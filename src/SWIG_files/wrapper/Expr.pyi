from typing import overload, NewType, Optional, Tuple

from OCC.Core.Expr import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.TCollection import *


class Expr:
	@staticmethod
	def CopyShare(self, exp: Expr_GeneralExpression) -> Expr_GeneralExpression: ...
	@staticmethod
	def NbOfFreeVariables(self, exp: Expr_GeneralExpression) -> int: ...
	@staticmethod
	def NbOfFreeVariables(self, exp: Expr_GeneralRelation) -> int: ...
	@staticmethod
	def Sign(self, val: float) -> float: ...

class Expr_GeneralExpression(Standard_Transient):
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def ContainsUnknowns(self) -> bool: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def EvaluateNumeric(self) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def IsShareable(self) -> bool: ...
	def NDerivative(self, X: Expr_NamedUnknown, N: int) -> Expr_GeneralExpression: ...
	def NbSubExpressions(self) -> int: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def Simplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...
	def SubExpression(self, I: int) -> Expr_GeneralExpression: ...

class Expr_GeneralFunction(Standard_Transient):
	def Copy(self) -> Expr_GeneralFunction: ...
	def Derivative(self, var: Expr_NamedUnknown) -> Expr_GeneralFunction: ...
	def Derivative(self, var: Expr_NamedUnknown, deg: int) -> Expr_GeneralFunction: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def GetStringName(self) -> TCollection_AsciiString: ...
	def IsIdentical(self, func: Expr_GeneralFunction) -> bool: ...
	def IsLinearOnVariable(self, index: int) -> bool: ...
	def NbOfVariables(self) -> int: ...
	def Variable(self, index: int) -> Expr_NamedUnknown: ...

class Expr_GeneralRelation(Standard_Transient):
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def Copy(self) -> Expr_GeneralRelation: ...
	def IsLinear(self) -> bool: ...
	def IsSatisfied(self) -> bool: ...
	def NbOfSingleRelations(self) -> int: ...
	def NbOfSubRelations(self) -> int: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def Simplified(self) -> Expr_GeneralRelation: ...
	def Simplify(self) -> None: ...
	def String(self) -> TCollection_AsciiString: ...
	def SubRelation(self, index: int) -> Expr_GeneralRelation: ...

class Expr_RUIterator:
	def __init__(self, rel: Expr_GeneralRelation) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Value(self) -> Expr_NamedUnknown: ...

class Expr_RelationIterator:
	def __init__(self, rel: Expr_GeneralRelation) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Value(self) -> Expr_SingleRelation: ...

class Expr_UnknownIterator:
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Value(self) -> Expr_NamedUnknown: ...

class Expr_BinaryExpression(Expr_GeneralExpression):
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def ContainsUnknowns(self) -> bool: ...
	def FirstOperand(self) -> Expr_GeneralExpression: ...
	def NbSubExpressions(self) -> int: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def SecondOperand(self) -> Expr_GeneralExpression: ...
	def SetFirstOperand(self, exp: Expr_GeneralExpression) -> None: ...
	def SetSecondOperand(self, exp: Expr_GeneralExpression) -> None: ...
	def Simplified(self) -> Expr_GeneralExpression: ...
	def SubExpression(self, I: int) -> Expr_GeneralExpression: ...

class Expr_FunctionDerivative(Expr_GeneralFunction):
	def __init__(self, func: Expr_GeneralFunction, withX: Expr_NamedUnknown, deg: int) -> None: ...
	def Copy(self) -> Expr_GeneralFunction: ...
	def Degree(self) -> int: ...
	def DerivVariable(self) -> Expr_NamedUnknown: ...
	def Derivative(self, var: Expr_NamedUnknown) -> Expr_GeneralFunction: ...
	def Derivative(self, var: Expr_NamedUnknown, deg: int) -> Expr_GeneralFunction: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, values: TColStd_Array1OfReal) -> float: ...
	def Expression(self) -> Expr_GeneralExpression: ...
	def Function(self) -> Expr_GeneralFunction: ...
	def GetStringName(self) -> TCollection_AsciiString: ...
	def IsIdentical(self, func: Expr_GeneralFunction) -> bool: ...
	def IsLinearOnVariable(self, index: int) -> bool: ...
	def NbOfVariables(self) -> int: ...
	def UpdateExpression(self) -> None: ...
	def Variable(self, index: int) -> Expr_NamedUnknown: ...

class Expr_NamedExpression(Expr_GeneralExpression):
	def GetName(self) -> TCollection_AsciiString: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsShareable(self) -> bool: ...
	def SetName(self, name: TCollection_AsciiString) -> None: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_NamedFunction(Expr_GeneralFunction):
	def __init__(self, name: TCollection_AsciiString, exp: Expr_GeneralExpression, vars: Expr_Array1OfNamedUnknown) -> None: ...
	def Copy(self) -> Expr_GeneralFunction: ...
	def Derivative(self, var: Expr_NamedUnknown) -> Expr_GeneralFunction: ...
	def Derivative(self, var: Expr_NamedUnknown, deg: int) -> Expr_GeneralFunction: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, values: TColStd_Array1OfReal) -> float: ...
	def Expression(self) -> Expr_GeneralExpression: ...
	def GetName(self) -> TCollection_AsciiString: ...
	def GetStringName(self) -> TCollection_AsciiString: ...
	def IsIdentical(self, func: Expr_GeneralFunction) -> bool: ...
	def IsLinearOnVariable(self, index: int) -> bool: ...
	def NbOfVariables(self) -> int: ...
	def SetExpression(self, exp: Expr_GeneralExpression) -> None: ...
	def SetName(self, newname: TCollection_AsciiString) -> None: ...
	def Variable(self, index: int) -> Expr_NamedUnknown: ...

class Expr_NumericValue(Expr_GeneralExpression):
	def __init__(self, val: float) -> None: ...
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def ContainsUnknowns(self) -> bool: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def GetValue(self) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def NDerivative(self, X: Expr_NamedUnknown, N: int) -> Expr_GeneralExpression: ...
	def NbSubExpressions(self) -> int: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def SetValue(self, val: float) -> None: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def Simplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...
	def SubExpression(self, I: int) -> Expr_GeneralExpression: ...

class Expr_PolyExpression(Expr_GeneralExpression):
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def ContainsUnknowns(self) -> bool: ...
	def NbOperands(self) -> int: ...
	def NbSubExpressions(self) -> int: ...
	def Operand(self, index: int) -> Expr_GeneralExpression: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def SetOperand(self, exp: Expr_GeneralExpression, index: int) -> None: ...
	def Simplified(self) -> Expr_GeneralExpression: ...
	def SubExpression(self, I: int) -> Expr_GeneralExpression: ...

class Expr_SingleRelation(Expr_GeneralRelation):
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def FirstMember(self) -> Expr_GeneralExpression: ...
	def IsLinear(self) -> bool: ...
	def NbOfSingleRelations(self) -> int: ...
	def NbOfSubRelations(self) -> int: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def SecondMember(self) -> Expr_GeneralExpression: ...
	def SetFirstMember(self, exp: Expr_GeneralExpression) -> None: ...
	def SetSecondMember(self, exp: Expr_GeneralExpression) -> None: ...
	def SubRelation(self, index: int) -> Expr_GeneralRelation: ...

class Expr_SystemRelation(Expr_GeneralRelation):
	def __init__(self, relation: Expr_GeneralRelation) -> None: ...
	def Add(self, relation: Expr_GeneralRelation) -> None: ...
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def Copy(self) -> Expr_GeneralRelation: ...
	def IsLinear(self) -> bool: ...
	def IsSatisfied(self) -> bool: ...
	def NbOfSingleRelations(self) -> int: ...
	def NbOfSubRelations(self) -> int: ...
	def Remove(self, relation: Expr_GeneralRelation) -> None: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def Simplified(self) -> Expr_GeneralRelation: ...
	def Simplify(self) -> None: ...
	def String(self) -> TCollection_AsciiString: ...
	def SubRelation(self, index: int) -> Expr_GeneralRelation: ...

class Expr_UnaryExpression(Expr_GeneralExpression):
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def ContainsUnknowns(self) -> bool: ...
	def NbSubExpressions(self) -> int: ...
	def Operand(self) -> Expr_GeneralExpression: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def SetOperand(self, exp: Expr_GeneralExpression) -> None: ...
	def Simplified(self) -> Expr_GeneralExpression: ...
	def SubExpression(self, I: int) -> Expr_GeneralExpression: ...

class Expr_Absolute(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_ArcCosine(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_ArcSine(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_ArcTangent(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_ArgCosh(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_ArgSinh(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_ArgTanh(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_BinaryFunction(Expr_BinaryExpression):
	def __init__(self, func: Expr_GeneralFunction, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def Function(self) -> Expr_GeneralFunction: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Cosh(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Cosine(Expr_UnaryExpression):
	def __init__(self, Exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Difference(Expr_BinaryExpression):
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def NDerivative(self, X: Expr_NamedUnknown, N: int) -> Expr_GeneralExpression: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Different(Expr_SingleRelation):
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralRelation: ...
	def IsSatisfied(self) -> bool: ...
	def Simplified(self) -> Expr_GeneralRelation: ...
	def Simplify(self) -> None: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Division(Expr_BinaryExpression):
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Equal(Expr_SingleRelation):
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralRelation: ...
	def IsSatisfied(self) -> bool: ...
	def Simplified(self) -> Expr_GeneralRelation: ...
	def Simplify(self) -> None: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Exponential(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Exponentiate(Expr_BinaryExpression):
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_GreaterThan(Expr_SingleRelation):
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralRelation: ...
	def IsSatisfied(self) -> bool: ...
	def Simplified(self) -> Expr_GeneralRelation: ...
	def Simplify(self) -> None: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_GreaterThanOrEqual(Expr_SingleRelation):
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralRelation: ...
	def IsSatisfied(self) -> bool: ...
	def Simplified(self) -> Expr_GeneralRelation: ...
	def Simplify(self) -> None: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_LessThan(Expr_SingleRelation):
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralRelation: ...
	def IsSatisfied(self) -> bool: ...
	def Simplified(self) -> Expr_GeneralRelation: ...
	def Simplify(self) -> None: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_LessThanOrEqual(Expr_SingleRelation):
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralRelation: ...
	def IsSatisfied(self) -> bool: ...
	def Simplified(self) -> Expr_GeneralRelation: ...
	def Simplify(self) -> None: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_LogOf10(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_LogOfe(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_NamedConstant(Expr_NamedExpression):
	def __init__(self, name: TCollection_AsciiString, value: float) -> None: ...
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def ContainsUnknowns(self) -> bool: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def GetValue(self) -> float: ...
	def IsLinear(self) -> bool: ...
	def NDerivative(self, X: Expr_NamedUnknown, N: int) -> Expr_GeneralExpression: ...
	def NbSubExpressions(self) -> int: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def Simplified(self) -> Expr_GeneralExpression: ...
	def SubExpression(self, I: int) -> Expr_GeneralExpression: ...

class Expr_NamedUnknown(Expr_NamedExpression):
	def __init__(self, name: TCollection_AsciiString) -> None: ...
	def Assign(self, exp: Expr_GeneralExpression) -> None: ...
	def AssignedExpression(self) -> Expr_GeneralExpression: ...
	def Contains(self, exp: Expr_GeneralExpression) -> bool: ...
	def ContainsUnknowns(self) -> bool: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Deassign(self) -> None: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsAssigned(self) -> bool: ...
	def IsLinear(self) -> bool: ...
	def NbSubExpressions(self) -> int: ...
	def Replace(self, var: Expr_NamedUnknown, with_: Expr_GeneralExpression) -> None: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def Simplified(self) -> Expr_GeneralExpression: ...
	def SubExpression(self, I: int) -> Expr_GeneralExpression: ...

class Expr_PolyFunction(Expr_PolyExpression):
	def __init__(self, func: Expr_GeneralFunction, exps: Expr_Array1OfGeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def Function(self) -> Expr_GeneralFunction: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Product(Expr_PolyExpression):
	@overload
	def __init__(self, exps: Expr_SequenceOfGeneralExpression) -> None: ...
	@overload
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Sine(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Sinh(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Square(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_SquareRoot(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Sum(Expr_PolyExpression):
	@overload
	def __init__(self, exps: Expr_SequenceOfGeneralExpression) -> None: ...
	@overload
	def __init__(self, exp1: Expr_GeneralExpression, exp2: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def NDerivative(self, X: Expr_NamedUnknown, N: int) -> Expr_GeneralExpression: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Tangent(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_Tanh(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_UnaryFunction(Expr_UnaryExpression):
	def __init__(self, func: Expr_GeneralFunction, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def Function(self) -> Expr_GeneralFunction: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...

class Expr_UnaryMinus(Expr_UnaryExpression):
	def __init__(self, exp: Expr_GeneralExpression) -> None: ...
	def Copy(self) -> Expr_GeneralExpression: ...
	def Derivative(self, X: Expr_NamedUnknown) -> Expr_GeneralExpression: ...
	def Evaluate(self, vars: Expr_Array1OfNamedUnknown, vals: TColStd_Array1OfReal) -> float: ...
	def IsIdentical(self, Other: Expr_GeneralExpression) -> bool: ...
	def IsLinear(self) -> bool: ...
	def NDerivative(self, X: Expr_NamedUnknown, N: int) -> Expr_GeneralExpression: ...
	def ShallowSimplified(self) -> Expr_GeneralExpression: ...
	def String(self) -> TCollection_AsciiString: ...
