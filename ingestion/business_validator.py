import pandas as pd

class BusinessValidator:
    def _init_(self, df: pd.DataFrame):
        self.df = df.copy()
        self.issues = []

    def validate_sales(self):
        invalid = self.df[self.df["Sales"] < 0]
        if not invalid.empty:
            self.issues.append(f"❌ Negative Sales: {len(invalid)} rows")

    def validate_profit(self):
        invalid = self.df[self.df["Profit"] < -10000]
        if not invalid.empty:
            self.issues.append(f"❌ Extreme Profit loss: {len(invalid)} rows")

    def validate_discount(self):
        invalid = self.df[(self.df["Discount"] < 0) | (self.df["Discount"] > 1)]
        if not invalid.empty:
            self.issues.append(f"❌ Invalid Discount: {len(invalid)} rows")

    def validate_quantity(self):
        invalid = self.df[self.df["Quantity"] <= 0]
        if not invalid.empty:
            self.issues.append(f"❌ Invalid Quantity: {len(invalid)} rows")

    def run_all_checks(self):
        print("\n==============================")
        print("💼 BUSINESS RULE VALIDATION")
        print("==============================")

        self.validate_sales()
        self.validate_profit()
        self.validate_discount()
        self.validate_quantity()

        if not self.issues:
            print("✅ No business rule violations found!")
        else:
            print("\n⚠️ ISSUES FOUND:")
            for i in self.issues:
                print(i)

        return self.issues