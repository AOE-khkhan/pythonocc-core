from typing import overload, NewType, Optional, Tuple

from OCC.Core.StdSelect import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.SelectMgr import *
from OCC.Core.Prs3d import *
from OCC.Core.TopoDS import *
from OCC.Core.PrsMgr import *
from OCC.Core.TopLoc import *
from OCC.Core.V3d import *
from OCC.Core.Select3D import *
from OCC.Core.TopAbs import *
from OCC.Core.Graphic3d import *
from OCC.Core.Geom import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *
from OCC.Core.Image import *


class StdSelect_TypeOfResult:
	StdSelect_TOR_SIMPLE: int = ...
	StdSelect_TOR_MULTIPLE: int = ...

class StdSelect_SensitivityMode:
	StdSelect_SM_WINDOW: int = ...
	StdSelect_SM_VIEW: int = ...

class StdSelect_TypeOfFace:
	StdSelect_AnyFace: int = ...
	StdSelect_Plane: int = ...
	StdSelect_Cylinder: int = ...
	StdSelect_Sphere: int = ...
	StdSelect_Torus: int = ...
	StdSelect_Revol: int = ...
	StdSelect_Cone: int = ...

class StdSelect_TypeOfEdge:
	StdSelect_AnyEdge: int = ...
	StdSelect_Line: int = ...
	StdSelect_Circle: int = ...

class StdSelect_DisplayMode:
	StdSelect_DM_Wireframe: int = ...
	StdSelect_DM_Shading: int = ...
	StdSelect_DM_HLR: int = ...

class StdSelect_TypeOfSelectionImage:
	StdSelect_TypeOfSelectionImage_NormalizedDepth: int = ...
	StdSelect_TypeOfSelectionImage_NormalizedDepthInverted: int = ...
	StdSelect_TypeOfSelectionImage_UnnormalizedDepth: int = ...
	StdSelect_TypeOfSelectionImage_ColoredDetectedObject: int = ...
	StdSelect_TypeOfSelectionImage_ColoredEntity: int = ...
	StdSelect_TypeOfSelectionImage_ColoredOwner: int = ...
	StdSelect_TypeOfSelectionImage_ColoredSelectionMode: int = ...

class StdSelect:
	@staticmethod
	def SetDrawerForBRepOwner(self, aSelection: SelectMgr_Selection, aDrawer: Prs3d_Drawer) -> None: ...

class StdSelect_BRepOwner(SelectMgr_EntityOwner):
	@overload
	def __init__(self, aPriority: int) -> None: ...
	@overload
	def __init__(self, aShape: TopoDS_Shape, aPriority: Optional[int], ComesFromDecomposition: Optional[bool]) -> None: ...
	@overload
	def __init__(self, aShape: TopoDS_Shape, theOrigin: SelectMgr_SelectableObject, aPriority: Optional[int], FromDecomposition: Optional[bool]) -> None: ...
	def Clear(self, aPM: PrsMgr_PresentationManager, aMode: Optional[int]) -> None: ...
	def HasHilightMode(self) -> bool: ...
	def HasShape(self) -> bool: ...
	def HilightMode(self) -> int: ...
	def HilightWithColor(self, thePM: PrsMgr_PresentationManager3d, theStyle: Prs3d_Drawer, theMode: Optional[int]) -> None: ...
	def IsHilighted(self, aPM: PrsMgr_PresentationManager, aMode: Optional[int]) -> bool: ...
	def ResetHilightMode(self) -> None: ...
	def SetHilightMode(self, theMode: int) -> None: ...
	def SetLocation(self, aLoc: TopLoc_Location) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Unhilight(self, aPM: PrsMgr_PresentationManager, aMode: Optional[int]) -> None: ...
	def UpdateHighlightTrsf(self, theViewer: V3d_Viewer, theManager: PrsMgr_PresentationManager3d, theDispMode: int) -> None: ...

class StdSelect_BRepSelectionTool:
	@staticmethod
	def ComputeSensitive(self, theShape: TopoDS_Shape, theOwner: SelectMgr_EntityOwner, theSelection: SelectMgr_Selection, theDeflection: float, theDeflAngle: float, theNbPOnEdge: int, theMaxiParam: float, theAutoTriang: Optional[bool]) -> None: ...
	@staticmethod
	def GetEdgeSensitive(self, theShape: TopoDS_Shape, theOwner: SelectMgr_EntityOwner, theSelection: SelectMgr_Selection, theDeflection: float, theDeviationAngle: float, theNbPOnEdge: int, theMaxiParam: float, theSensitive: Select3D_SensitiveEntity) -> None: ...
	@staticmethod
	def GetSensitiveForFace(self, theFace: TopoDS_Face, theOwner: SelectMgr_EntityOwner, theOutList: Select3D_EntitySequence, theAutoTriang: Optional[bool], theNbPOnEdge: Optional[int], theMaxiParam: Optional[float], theInteriorFlag: Optional[bool]) -> bool: ...
	@staticmethod
	def GetStandardPriority(self, theShape: TopoDS_Shape, theType: TopAbs_ShapeEnum) -> int: ...
	@staticmethod
	def Load(self, aSelection: SelectMgr_Selection, aShape: TopoDS_Shape, aType: TopAbs_ShapeEnum, theDeflection: float, theDeviationAngle: float, AutoTriangulation: Optional[bool], aPriority: Optional[int], NbPOnEdge: Optional[int], MaximalParameter: Optional[float]) -> None: ...
	@staticmethod
	def Load(self, aSelection: SelectMgr_Selection, Origin: SelectMgr_SelectableObject, aShape: TopoDS_Shape, aType: TopAbs_ShapeEnum, theDeflection: float, theDeviationAngle: float, AutoTriangulation: Optional[bool], aPriority: Optional[int], NbPOnEdge: Optional[int], MaximalParameter: Optional[float]) -> None: ...
	@staticmethod
	def PreBuildBVH(self, theSelection: SelectMgr_Selection) -> None: ...

class StdSelect_EdgeFilter(SelectMgr_Filter):
	def __init__(self, Edge: StdSelect_TypeOfEdge) -> None: ...
	def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
	def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...
	def SetType(self, aNewType: StdSelect_TypeOfEdge) -> None: ...
	def Type(self) -> StdSelect_TypeOfEdge: ...

class StdSelect_FaceFilter(SelectMgr_Filter):
	def __init__(self, aTypeOfFace: StdSelect_TypeOfFace) -> None: ...
	def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
	def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...
	def SetType(self, aNewType: StdSelect_TypeOfFace) -> None: ...
	def Type(self) -> StdSelect_TypeOfFace: ...

class StdSelect_Prs(Prs3d_Presentation):
	def __init__(self, aStructureManager: Graphic3d_StructureManager) -> None: ...
	def Manager(self) -> Graphic3d_StructureManager: ...

class StdSelect_Shape(PrsMgr_PresentableObject):
	def __init__(self, theShape: TopoDS_Shape, theDrawer: Optional[Prs3d_Drawer]) -> None: ...
	def Compute(self, aPresentationManager: PrsMgr_PresentationManager3d, aPresentation: Prs3d_Presentation, aMode: Optional[int]) -> None: ...
	def Compute(self, aProjector: Prs3d_Projector, aTrsf: Geom_Transformation, aPresentation: Prs3d_Presentation) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Shape(self, theShape: TopoDS_Shape) -> None: ...

class StdSelect_ShapeTypeFilter(SelectMgr_Filter):
	def __init__(self, aType: TopAbs_ShapeEnum) -> None: ...
	def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
	def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...
	def Type(self) -> TopAbs_ShapeEnum: ...

class StdSelect_ViewerSelector3d(SelectMgr_ViewerSelector):
	def __init__(self) -> None: ...
	def ClearSensitive(self, theView: V3d_View) -> None: ...
	def DisplaySensitive(self, theView: V3d_View) -> None: ...
	def DisplaySensitive(self, theSel: SelectMgr_Selection, theTrsf: gp_Trsf, theView: V3d_View, theToClearOthers: Optional[bool]) -> None: ...
	def Pick(self, theXPix: int, theYPix: int, theView: V3d_View) -> None: ...
	def Pick(self, theXPMin: int, theYPMin: int, theXPMax: int, theYPMax: int, theView: V3d_View) -> None: ...
	def Pick(self, thePolyline: TColgp_Array1OfPnt2d, theView: V3d_View) -> None: ...
	def PixelTolerance(self) -> int: ...
	def SetPixelTolerance(self, theTolerance: int) -> None: ...
	def ToPixMap(self, theImage: Image_PixMap, theView: V3d_View, theType: StdSelect_TypeOfSelectionImage, thePickedIndex: Optional[int]) -> bool: ...
