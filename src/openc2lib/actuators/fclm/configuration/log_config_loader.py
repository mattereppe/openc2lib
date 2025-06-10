import os, json, logging
from openc2lib.profiles.fclm.data.ef import EF
from openc2lib import ArrayOf
#define Nothing as a string
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env
Empty= ["Nothing"]
logger = logging.getLogger(__name__)

class LogConfigLoader:
    
    def _load_log_config(self, config_filename):
        """
        Load log configuration from a JSON file and return specific details based on asset_id and feature_name.
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
        :param asset_id: The ID of the asset to query (e.g., "agent_x").
        :param feature_name: The name of the feature to query (e.g., "import_configs").
        :return: The feature value or Nothing if the feature is not found.
        """
        config = self._load_log_config("CAPABILITIES_CONFIG")
        if config and asset_id in config:
            asset_config = config[asset_id]
            feature_value = asset_config.get(feature_name)
            if feature_value:
                return feature_value
            else:
                return Empty  # Feature not found
        return Empty  # Asset ID not found

    def get_export_fields(self, asset_id, ef_names_to_return: ArrayOf=None):
        """
        Get the information elements (EF) for the specified asset_id and its agent.
        If specific ef_names are provided, return those agent-specific EFs, else return the general EFs.
        
        :param asset_id: The ID of the asset to query for EFs.
        :param ef_names_to_return: A list of specific ef_names to return, or None to return all general efs.
        :return: A tuple of (ArrayOf(EF), list of ef_names) or an error message if any element is not found.
        """
        export_fields = self._load_log_config("EXPORT_FIELDS_CONFIG")
        agent = self.get_feature(asset_id=asset_id, feature_name='agent')
        if agent == Empty:
            return Empty

        efs = ArrayOf(EF)()
        ef_names = []

        if ef_names_to_return is not None:
            # If the specific ef_names_to_return list is provided
            for ef_name in ef_names_to_return:
                # Look for the ef name in the configuration
                if ef_name in export_fields:
                    agent_map = export_fields[ef_name]
                    if agent in agent_map:
                        ef_names.append(agent_map[agent])  # Add the agent-specific EF
                    else:
                        return None
                else:
                    return None
            return ef_names
        else:
            # If no specific ef_names are provided, return general EFs
            for ef_name, agent_map in export_fields.items():
                if agent in agent_map:
                    efs.append(EF(ef_name))  # Collect general ef_names
            return efs  # Return both the populated ArrayOf(EF) and list of ef_names


