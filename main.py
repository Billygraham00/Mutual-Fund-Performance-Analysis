import pandas as pd
import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore")

from log_code import setup_logging
logger = setup_logging("mutual_fund_data_cleaning")


class MUTUAL_FUND_DATA_CLEANING:

    def __init__(self, path):
        try:
            self.df = pd.read_csv(path)
            self.df.columns = self.df.columns.str.strip()
            logger.info("CSV file loaded successfully")
            logger.info(f"Dataset shape: {self.df.shape}")
        except Exception as e:
            logger.error(f"Error loading CSV file: {e}")
            raise

    def clean_data(self):
        try:
            df = self.df

            # ---------------- Replace '-' with NaN ----------------
            df.replace('-', np.nan, inplace=True)
            logger.info("Replaced '-' with NaN")

            # ---------------- Percentage columns ----------------
            percent_columns = [
                'ExpenseRatio (%)','Turnover Ratio (%)','Yield To Maturity (%)',
                'Return (%)1 mo','Return (%)3 mo','Return (%)6 mo',
                'Return (%)1 yr','Return (%)2 yrs','Return (%)3 yrs',
                'Return (%)5 yrs','Return (%)10 yrs',
                'Large Cap(%)','Mid Cap(%)','Small Cap(%)'
            ]

            for col in percent_columns:
                if col in df.columns:
                    df[col] = df[col].astype(str).str.replace('%', '', regex=False).astype(float)

            logger.info("Converted percentage columns to numeric")

            # ---------------- Risk metric columns ----------------
            risk_columns = ['Alpha','Sharpe','Sortino','Beta','Standard Deviation']

            for col in risk_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            logger.info("Converted risk metric columns to numeric")

            # ---------------- Debt-specific columns ----------------
            debt_columns = ['Avg. Maturity(in yrs)','Mod. Duration(in yrs)']

            for col in debt_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            logger.info("Converted debt-specific columns to numeric")

            # ---------------- Other numeric columns ----------------
            numeric_columns = [
                'AUM(in Rs. cr)','NAV','52 WeekHigh (NAV)','52 WeekLow (NAV)',
                'No. ofStocks','Avg. Market Cap(in Rs. cr)'
            ]

            for col in numeric_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            logger.info("Converted remaining numeric columns")

            # ---------------- Date column ----------------
            if 'Inception Date' in df.columns:
                df['Inception Date'] = pd.to_datetime(df['Inception Date'], errors='coerce')

            logger.info("Converted Inception Date to datetime")

            # ---------------- Exit load handling ----------------
            if 'Exit_load_Remarks' in df.columns:
                df['Exit_load_Remarks'] = (
                    df['Exit_load_Remarks']
                    .replace(['-', 'Nil', 'nil', 'NIL', ''], np.nan)
                    .str.strip()
                    .fillna('No Exit Load')
                )
                logger.info("Standardized Exit_load_Remarks and filled blanks with 'No Exit Load'")

            # ---------------- Duplicate check ----------------
            dup_rows = df.duplicated().sum()
            dup_funds = df['Funds'].duplicated().sum()

            logger.info(f"Duplicate rows count: {dup_rows}")
            logger.info(f"Duplicate fund names count: {dup_funds}")

            # ---------------- Benchmark Index null check ----------------
            if 'Benchmark Index' in df.columns:
                df['Benchmark Index'] = (
                    df['Benchmark Index']
                    .replace(['-', 'Nil', 'nil', 'NIL', '', 'null'], np.nan)
                    .str.strip()
                    .fillna('No Exit Load')
                )
                logger.info("Standardized Benchmark Index and filled blanks with 'Not Applicable'")

            self.df = df
            logger.info("Data cleaning completed successfully")

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logger.error(f"Error in line {exc_tb.tb_lineno}: {exc_obj}")
            raise

    def save_cleaned_data(self, output_path):
        try:
            self.df.to_csv(output_path, index=False)
            logger.info(f"Cleaned dataset saved at: {output_path}")
        except Exception as e:
            logger.error(f"Error saving cleaned data: {e}")
            raise


# ================= MAIN EXECUTION =================
if __name__ == "__main__":

    obj = MUTUAL_FUND_DATA_CLEANING(
        r"D:\Mutual Fund Performance_Project\Mutual Fund Dataset1 2025.csv"
    )

    obj.clean_data()

    obj.save_cleaned_data(
        r"D:\Mutual Fund Performance_Project\Mutual_Fund_Cleaned.csv"
    )
