"""Calc-3 visitor scaffold.

Initial skeleton only. Evaluation semantics are intentionally not implemented.
"""

from CalcPlusVisitor import CalcPlusVisitor


class Calc3Visitor(CalcPlusVisitor):
    """Project-specific visitor scaffold for Calc-3."""

    def __init__(self):
        super().__init__()
        # TODO: initialize runtime state (e.g., symbol table, outputs).
        self.env = {}

    def visitCalc3(self, ctx):
        """Entry point placeholder for program evaluation."""
        # TODO: implement full statement execution order and return contract.
        raise NotImplementedError("Calc3Visitor is a scaffold; semantics not implemented yet.")
