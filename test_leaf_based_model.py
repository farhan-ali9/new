import unittest
from leaf_based_model import LeafBasedModel  # Replace 'your_module' with the actual module name

class TestLeafBasedModel(unittest.TestCase):

    def setUp(self):
        # Initialize the LeafBasedModel instance for testing
        self.base_folder = "//home/farhan/FIverr project/unit_tests/unit_tests"
        self.model_config = {
            "path_performance": self.base_folder + "/performance/",
            "path_features_folder": self.base_folder + "/price_data/",
            "path_sentiment_folder": self.base_folder + "/sent_write_path_tables_2022-12-31/",
            "path_company_names": self.base_folder + "/mapping_companies_unit_tests.xlsx",
        }
        self.LBM = LeafBasedModel(
            self.model_config["path_features_folder"],
            self.model_config["path_sentiment_folder"],
            self.model_config["path_company_names"],
            self.model_config["path_performance"],
            "end_date",
        )
        self.LBM.firms = ["ABB","Adecco","Alcon","Baloise","Banque Cantonale Vaudoise BCV","Barry Callebaut","Basilea","BELIMO","CS Group","Clariant","DKSH"]
        self.LBM.data_all={}
        

    def test_compute_cap_weights(self):
        # Test the compute_cap_weights method
        self.LBM.compute_cap_weights()
        # Add assertions to verify the expected behavior

    def test_compute_threshold(self):
        # Test the compute_threshold method
        self.LBM.compute_threshold()
        # Add assertions to verify the expected behavior

    def test_compute_historical_performance(self):
        # Test the compute_historical_performance method
        self.LBM.compute_historical_performance()
        # Add assertions to verify the expected behavior

    def test_rank_models(self):
        # Test the rank_models method
        self.LBM.rank_models()
        # Add assertions to verify the expected behavior

    def test_performance_test(self):
        # Test the performance_test method
        df_companies_test = self.LBM.performance_test()
        # Add assertions to verify the expected behavior of df_companies_test

    def test_store(self):
        # Test the store method
        self.LBM.store()
        # Add assertions to verify the expected behavior

if __name__ == "__main__":
    unittest.main()

