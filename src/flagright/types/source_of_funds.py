# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SourceOfFunds(str, enum.Enum):
    EARNINGS = "Earnings"
    SAVINGS = "Savings"
    INVESTMENTS_DEPOSITS = "Investments/Deposits"
    WEALTH = "Wealth"
    GIFT = "Gift"
    PENSION = "Pension"
    INHERITANCE = "Inheritance"
    GAMBLING = "Gambling"
    BENEFITS = "Benefits"
    PASSIVE = "Passive"
    FAMILY = "Family"
    INSURANCE = "Insurance"
    LEGAL = "Legal"
    SALES = "Sales"
    ROLLOVER = "Rollover"
    EQUITY = "Equity"
    CRYPTO = "Crypto"
    BUSINESS = "Business"
    EMPLOYMENT = "Employment"

    def visit(
        self,
        earnings: typing.Callable[[], T_Result],
        savings: typing.Callable[[], T_Result],
        investments_deposits: typing.Callable[[], T_Result],
        wealth: typing.Callable[[], T_Result],
        gift: typing.Callable[[], T_Result],
        pension: typing.Callable[[], T_Result],
        inheritance: typing.Callable[[], T_Result],
        gambling: typing.Callable[[], T_Result],
        benefits: typing.Callable[[], T_Result],
        passive: typing.Callable[[], T_Result],
        family: typing.Callable[[], T_Result],
        insurance: typing.Callable[[], T_Result],
        legal: typing.Callable[[], T_Result],
        sales: typing.Callable[[], T_Result],
        rollover: typing.Callable[[], T_Result],
        equity: typing.Callable[[], T_Result],
        crypto: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        employment: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SourceOfFunds.EARNINGS:
            return earnings()
        if self is SourceOfFunds.SAVINGS:
            return savings()
        if self is SourceOfFunds.INVESTMENTS_DEPOSITS:
            return investments_deposits()
        if self is SourceOfFunds.WEALTH:
            return wealth()
        if self is SourceOfFunds.GIFT:
            return gift()
        if self is SourceOfFunds.PENSION:
            return pension()
        if self is SourceOfFunds.INHERITANCE:
            return inheritance()
        if self is SourceOfFunds.GAMBLING:
            return gambling()
        if self is SourceOfFunds.BENEFITS:
            return benefits()
        if self is SourceOfFunds.PASSIVE:
            return passive()
        if self is SourceOfFunds.FAMILY:
            return family()
        if self is SourceOfFunds.INSURANCE:
            return insurance()
        if self is SourceOfFunds.LEGAL:
            return legal()
        if self is SourceOfFunds.SALES:
            return sales()
        if self is SourceOfFunds.ROLLOVER:
            return rollover()
        if self is SourceOfFunds.EQUITY:
            return equity()
        if self is SourceOfFunds.CRYPTO:
            return crypto()
        if self is SourceOfFunds.BUSINESS:
            return business()
        if self is SourceOfFunds.EMPLOYMENT:
            return employment()
