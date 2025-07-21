import ast
import operator
import math
from statistics import mean, median, stdev
from django.shortcuts import render
from django.views import View

OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod, ast.USub: operator.neg,
}
FUNCS = {
    'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
    'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
    'sqrt': math.sqrt, 'log': math.log, 'log10': math.log10, 'exp': math.exp, 'factorial': math.factorial,
    'abs': abs, 'mean': lambda *a: mean(a), 'median': lambda *a: median(a),
    'stdev': lambda *a: stdev(a) if len(a) > 1 else float('nan'),
    'compound_interest': lambda p,r,n,t: p * (1 + r/n) ** (n*t),
}
CONSTANTS = { 'pi': math.pi, 'e': math.e }

class Eval(ast.NodeVisitor):
    def visit(self, node):
        if isinstance(node, ast.Expression): return self.visit(node.body)
        elif isinstance(node, ast.Num): return node.n
        elif isinstance(node, ast.BinOp): return OPS[type(node.op)](self.visit(node.left), self.visit(node.right))
        elif isinstance(node, ast.UnaryOp): return OPS[type(node.op)](self.visit(node.operand))
        elif isinstance(node, ast.Call):
            fname = node.func.id
            args = [self.visit(arg) for arg in node.args]
            if fname in FUNCS: return FUNCS[fname](*args)
            raise ValueError("Unsupported function: "+fname)
        elif isinstance(node, ast.Name):
            if node.id in CONSTANTS: return CONSTANTS[node.id]
            raise ValueError("Unknown variable/constant: "+node.id)
        else: raise ValueError("Unsupported syntax")
    @classmethod
    def eval_expr(cls, expr, deg_mode=True):
        expr = expr.replace('^','**')
        if deg_mode:
            expr = expr.replace('sin(','sin(math.radians(')\
                               .replace('cos(','cos(math.radians(')\
                               .replace('tan(','tan(math.radians(')
        return cls().visit(ast.parse(expr, mode='eval'))

class CalculatorView(View):
    def get(self, request):
        return render(request, "calculator_app.html")
    def post(self, request):
        expr = request.POST.get("expression","")
        deg_mode = request.POST.get("deg_mode","1") == "1"
        result, error = "", ""
        if expr:
            try:
                result = Eval.eval_expr(expr, deg_mode)
            except Exception as ex:
                error = str(ex)
        return render(request, "calculator_app.html", {
            "expression": expr, "result": result, "error": error, "deg_mode": deg_mode
        })
