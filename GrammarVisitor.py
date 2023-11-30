# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ifStatement.
    def visitIfStatement(self, ctx:GrammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#switchStatement.
    def visitSwitchStatement(self, ctx:GrammarParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assignment.
    def visitAssignment(self, ctx:GrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forLoop.
    def visitForLoop(self, ctx:GrammarParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#condition.
    def visitCondition(self, ctx:GrammarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)



del GrammarParser