from typing import overload, NewType, Optional, Tuple

from OCC.Core.BVH import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *


class BVH_AxisSelector:
	@staticmethod
	def MainAxis(self, theSize: BVH_VecNt) -> int: ...

class BVH_Tree():
	def __init__(self) -> None: ...
	def AddInnerNode(self, theMinPoint: BVH_VecNt, theMaxPoint: BVH_VecNt, theLftChild: int, theRghChild: int) -> False: ...
	def AddInnerNode(self, theLftChild: int, theRghChild: int) -> False: ...
	def AddLeafNode(self, theMinPoint: BVH_VecNt, theMaxPoint: BVH_VecNt, theBegElem: int, theEndElem: int) -> False: ...
	def AddLeafNode(self, theBegElem: int, theEndElem: int) -> False: ...
	def Clear(self) -> None: ...
	def CollapseToQuadTree(self) -> False: ...
	def EstimateSAH(self) -> False: ...
	def Reserve(self, theNbNodes: int) -> None: ...
	def SetInner(self, theNodeIndex: int) -> None: ...
	def SetOuter(self, theNodeIndex: int) -> None: ...

class BVH_Tree():
	def __init__(self) -> None: ...
