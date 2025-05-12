import os, json, logging
from openc2lib.profiles.nfm.data.ie import IE
from openc2lib import ArrayOf
#define Nothing as a string
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env
Nothing: str = ["Nothing"]
logger = logging.getLogger(__name__)
class ProbeConfigLoader:
    
    def _load_probe_config(self, config_filename):
        """
        Load probe configuration from a JSON file and return specific details based on asset_id and feature_name.
        """
        try:
            config_file = os.getenv(config_filename)
            config_path = os.path.join(os.path.dirname(__file__), config_file)
            with open(config_path, 'r') as f:
                config = json.load(f)
                if config: 
                    return config
                else: 
                    return None
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load config: {e}")
            return None

    def get_feature(self, asset_id, feature_name):
        """
        Query for a specific feature for a given asset_id.
        :param asset_id: The ID of the asset to query (e.g., "probe_x").
        :param feature_name: The name of the feature to query (e.g., "flow_format").
        :return: The feature value or Nothing if the feature is not found.
        """
        config = self._load_probe_config("CAPABILITIES_CONFIG")
        if config and asset_id in config:
            asset_config = config[asset_id]
            feature_value = asset_config.get(feature_name)
            if feature_value:
                return feature_value
            else:
                return Nothing  # Feature not found
        return Nothing  # Asset ID not found

    def get_info_element(self, asset_id, ie_names_to_return: ArrayOf=None):
        """
        Get the information elements (IEs) for the specified asset_id and its agent.
        If specific ie_names are provided, return those agent-specific IEs, else return the general IEs.
        
        :param asset_id: The ID of the asset to query for IEs.
        :param ie_names_to_return: A list of specific ie_names to return, or None to return all general IEs.
        :return: A tuple of (ArrayOf(IE), list of ie_names) or an error message if any element is not found.
        """
        info_elems = self._load_probe_config("INFORMATION_ELEMENTS_CONFIG")
        agent = self.get_feature(asset_id=asset_id, feature_name='agent')
        if agent == Nothing:
            return Nothing

        ies = ArrayOf(IE)()
        ie_names = []

        if ie_names_to_return is not None:
            # If the specific ie_names_to_return list is provided
            for ie_name in ie_names_to_return:
                # Look for the IE name in the configuration
                if ie_name in info_elems:
                    agent_map = info_elems[ie_name]
                    if agent in agent_map:
                        ie_names.append(agent_map[agent])  # Add the agent-specific IE
                    else:
                        return None
                else:
                    return None
            return ie_names
        else:
            # If no specific ie_names are provided, return general IEs
            for ie_name, agent_map in info_elems.items():
                if agent in agent_map:
                    ies.append(IE(ie_name))  # Collect general ie_names
            return ies  # Return both the populated ArrayOf(IE) and list of ie_names


