from bmi_package import bmi_reports,count_overweight,getUpdatedTable
import json
import pandas as pd

# actual data file
RAW_DATA_FILE = 'rawData.json'

# test data file
RAW_TEST_DATA_FILE = 'rawTestData.json'


def test_count_overweight(filename):
    """
    This function is used for testing the edge cases

    """
    try:
        # Test Data Read #
        df = getUpdatedTable(filename)

        # Empty Dataframe test #
        df2 = pd.DataFrame()
        assert count_overweight(df2) is None, "Empty Dataframe"

        # Test Data checks #
        assert count_overweight(df) == 1, "Incorrect Count of Overweight"

        print('All tests passed !')

    except Exception as e:
        print(e)



if __name__ == '__main__':

    # Create the New Fields #
    filename = RAW_DATA_FILE
    df = getUpdatedTable(filename)

    # Count of Overweight #
    totalOverweight = count_overweight(df)
    print('Data :')
    print(df)
    print('\nThe total number of overweight are : ', totalOverweight)


    print("\n*** Test Results ***")
    filename = RAW_TEST_DATA_FILE
    test_count_overweight(filename)

