from typing import overload, NewType, Optional, Tuple

from OCC.Core.SelectMgr import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.PrsMgr import *
from OCC.Core.Graphic3d import *
from OCC.Core.Aspect import *
from OCC.Core.Prs3d import *
from OCC.Core.TopLoc import *
from OCC.Core.V3d import *
from OCC.Core.TopAbs import *
from OCC.Core.BVH import *
from OCC.Core.SelectBasics import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *
from OCC.Core.Select3D import *
from OCC.Core.Bnd import *

SelectBasics_EntityOwner = NewType('SelectBasics_EntityOwner', SelectMgr_EntityOwner)
SelectMgr_SOPtr = NewType('SelectMgr_SOPtr', SelectMgr_SelectableObject)

class SelectMgr_TypeOfUpdate:
	SelectMgr_TOU_Full: int = ...
	SelectMgr_TOU_Partial: int = ...
	SelectMgr_TOU_None: int = ...

class SelectMgr_TypeOfBVHUpdate:
	SelectMgr_TBU_Add: int = ...
	SelectMgr_TBU_Remove: int = ...
	SelectMgr_TBU_Renew: int = ...
	SelectMgr_TBU_Invalidate: int = ...
	SelectMgr_TBU_None: int = ...

class SelectMgr_StateOfSelection:
	SelectMgr_SOS_Any: int = ...
	SelectMgr_SOS_Unknown: int = ...
	SelectMgr_SOS_Deactivated: int = ...
	SelectMgr_SOS_Activated: int = ...

class SelectMgr_PickingStrategy:
	SelectMgr_PickingStrategy_FirstAcceptable: int = ...
	SelectMgr_PickingStrategy_OnlyTopmost: int = ...

class SelectMgr_EntityOwner(Standard_Transient):
	@overload
	def __init__(self, aPriority: Optional[int]) -> None: ...
	@overload
	def __init__(self, aSO: SelectMgr_SelectableObject, aPriority: Optional[int]) -> None: ...
	@overload
	def __init__(self, theOwner: SelectMgr_EntityOwner, aPriority: Optional[int]) -> None: ...
	def Clear(self, thePrsMgr: PrsMgr_PresentationManager, theMode: Optional[int]) -> None: ...
	def ComesFromDecomposition(self) -> bool: ...
	def HasLocation(self) -> bool: ...
	def HasSelectable(self) -> bool: ...
	def HilightWithColor(self, thePrsMgr: PrsMgr_PresentationManager, theStyle: Prs3d_Drawer, theMode: Optional[int]) -> None: ...
	def IsAutoHilight(self) -> bool: ...
	def IsForcedHilight(self) -> bool: ...
	def IsHilighted(self, thePrsMgr: PrsMgr_PresentationManager, theMode: Optional[int]) -> bool: ...
	def IsSameSelectable(self, theOther: SelectMgr_SelectableObject) -> bool: ...
	def IsSelected(self) -> bool: ...
	def Location(self) -> TopLoc_Location: ...
	def Priority(self) -> int: ...
	def Selectable(self) -> SelectMgr_SelectableObject: ...
	def Set(self, theSelObj: SelectMgr_SelectableObject) -> None: ...
	def Set(self, thePriority: int) -> None: ...
	def SetComesFromDecomposition(self, theIsFromDecomposition: bool) -> None: ...
	def SetLocation(self, theLocation: TopLoc_Location) -> None: ...
	def SetPriority(self, thePriority: int) -> None: ...
	def SetSelectable(self, theSelObj: SelectMgr_SelectableObject) -> None: ...
	def SetSelected(self, theIsSelected: bool) -> None: ...
	def State(self) -> int: ...
	def State(self, theStatus: int) -> None: ...
	def Unhilight(self, thePrsMgr: PrsMgr_PresentationManager, theMode: Optional[int]) -> None: ...
	def UpdateHighlightTrsf(self, theViewer: V3d_Viewer, theManager: PrsMgr_PresentationManager, theDispMode: int) -> None: ...

class SelectMgr_Filter(Standard_Transient):
	def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
	def IsOk(self, anObj: SelectMgr_EntityOwner) -> bool: ...

class SelectMgr_SelectableObject(PrsMgr_PresentableObject):
	def AcceptShapeDecomposition(self) -> bool: ...
	def AddSelection(self, aSelection: SelectMgr_Selection, aMode: int) -> None: ...
	def ClearDynamicHighlight(self, theMgr: PrsMgr_PresentationManager) -> None: ...
	def ClearSelected(self) -> None: ...
	def ClearSelections(self, update: Optional[bool]) -> None: ...
	def ComputeSelection(self, theSelection: SelectMgr_Selection, theMode: int) -> None: ...
	def CurrentSelection(self) -> SelectMgr_Selection: ...
	def ErasePresentations(self, theToRemove: bool) -> None: ...
	def GetAssemblyOwner(self) -> SelectMgr_EntityOwner: ...
	def GetHilightPresentation(self, thePrsMgr: PrsMgr_PresentationManager) -> Prs3d_Presentation: ...
	def GetSelectPresentation(self, thePrsMgr: PrsMgr_PresentationManager) -> Prs3d_Presentation: ...
	def GlobalSelOwner(self) -> SelectMgr_EntityOwner: ...
	def GlobalSelectionMode(self) -> int: ...
	def HasSelection(self, theMode: int) -> bool: ...
	def HilightOwnerWithColor(self, thePM: PrsMgr_PresentationManager, theStyle: Prs3d_Drawer, theOwner: SelectMgr_EntityOwner) -> None: ...
	def HilightSelected(self, thePrsMgr: PrsMgr_PresentationManager, theSeq: SelectMgr_SequenceOfOwner) -> None: ...
	def Init(self) -> None: ...
	def IsAutoHilight(self) -> bool: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def RecomputePrimitives(self) -> None: ...
	def RecomputePrimitives(self, theMode: int) -> None: ...
	def ResetTransformation(self) -> None: ...
	def Selection(self, theMode: int) -> SelectMgr_Selection: ...
	def Selections(self) -> SelectMgr_SequenceOfSelection: ...
	def SetAssemblyOwner(self, theOwner: SelectMgr_EntityOwner, theMode: Optional[int]) -> None: ...
	def SetAutoHilight(self, theAutoHilight: bool) -> None: ...
	def UpdateSelection(self, theMode: Optional[int]) -> None: ...
	def UpdateTransformation(self) -> None: ...
	def UpdateTransformations(self, aSelection: SelectMgr_Selection) -> None: ...

class SelectMgr_SelectableObjectSet:
	def __init__(self) -> None: ...
	def Append(self, theObject: SelectMgr_SelectableObject) -> bool: ...
	def ChangeSubset(self, theObject: SelectMgr_SelectableObject) -> None: ...
	def Contains(self, theObject: SelectMgr_SelectableObject) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def MarkDirty(self) -> None: ...
	def Remove(self, theObject: SelectMgr_SelectableObject) -> bool: ...
	def UpdateBVH(self, theCamera: Graphic3d_Camera, theProjectionMat: Graphic3d_Mat4d, theWorldViewMat: Graphic3d_Mat4d, theViewState: Graphic3d_WorldViewProjState, theViewportWidth: int, theViewportHeight: int) -> None: ...

class SelectMgr_SelectingVolumeManager(SelectBasics_SelectingVolumeManager):
	def __init__(self, theToAllocateFrustums: Optional[bool]) -> None: ...
	def AllowOverlapDetection(self, theIsToAllow: bool) -> None: ...
	def BuildSelectingVolume(self, thePoint: gp_Pnt2d) -> None: ...
	def BuildSelectingVolume(self, theMinPt: gp_Pnt2d, theMaxPt: gp_Pnt2d) -> None: ...
	def BuildSelectingVolume(self, thePoints: TColgp_Array1OfPnt2d) -> None: ...
	def Camera(self) -> Graphic3d_Camera: ...
	def DetectedPoint(self, theDepth: float) -> gp_Pnt: ...
	def DistToGeometryCenter(self, theCOG: gp_Pnt) -> float: ...
	def GetActiveSelectionType(self) -> int: ...
	def GetFarPickedPnt(self) -> gp_Pnt: ...
	def GetMousePosition(self) -> gp_Pnt2d: ...
	def GetNearPickedPnt(self) -> gp_Pnt: ...
	def GetVertices(self) -> gp_Pnt: ...
	def IsOverlapAllowed(self) -> bool: ...
	def ObjectClipping(self) -> Graphic3d_SequenceOfHClipPlane: ...
	def Overlaps(self, theBoxMin: SelectMgr_Vec3, theBoxMax: SelectMgr_Vec3, thePickResult: SelectBasics_PickResult) -> bool: ...
	def Overlaps(self, theBoxMin: SelectMgr_Vec3, theBoxMax: SelectMgr_Vec3, theInside: Optional[bool]) -> bool: ...
	def Overlaps(self, thePnt: gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool: ...
	def Overlaps(self, thePnt: gp_Pnt) -> bool: ...
	def Overlaps(self, theArrayOfPts: TColgp_HArray1OfPnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
	def Overlaps(self, theArrayOfPts: TColgp_Array1OfPnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
	def Overlaps(self, thePnt1: gp_Pnt, thePnt2: gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool: ...
	def Overlaps(self, thePnt1: gp_Pnt, thePnt2: gp_Pnt, thePnt3: gp_Pnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
	def ProjectionMatrix(self) -> Graphic3d_Mat4d: ...
	def ScaleAndTransform(self, theScaleFactor: int, theTrsf: gp_GTrsf, theBuilder: Optional[SelectMgr_FrustumBuilder]) -> SelectMgr_SelectingVolumeManager: ...
	def SetCamera(self, theCamera: Graphic3d_Camera) -> None: ...
	def SetCamera(self, theProjection: Graphic3d_Mat4d, theWorldView: Graphic3d_Mat4d, theIsOrthographic: bool, theWVPState: Optional[Graphic3d_WorldViewProjState]) -> None: ...
	def SetPixelTolerance(self, theTolerance: int) -> None: ...
	def SetViewClipRanges(self, theRange: SelectMgr_ViewClipRange) -> None: ...
	def SetViewClipping(self, theViewPlanes: Graphic3d_SequenceOfHClipPlane, theObjPlanes: Graphic3d_SequenceOfHClipPlane) -> None: ...
	def SetViewClipping(self, theOther: SelectMgr_SelectingVolumeManager) -> None: ...
	def SetViewport(self, theX: float, theY: float, theWidth: float, theHeight: float) -> None: ...
	def SetWindowSize(self, theWidth: int, theHeight: int) -> None: ...
	def ViewClipRanges(self) -> SelectMgr_ViewClipRange: ...
	def ViewClipping(self) -> Graphic3d_SequenceOfHClipPlane: ...
	def WindowSize(self) -> Tuple[int, int]: ...
	def WorldViewMatrix(self) -> Graphic3d_Mat4d: ...
	def WorldViewProjState(self) -> Graphic3d_WorldViewProjState: ...

class SelectMgr_Selection(Standard_Transient):
	def __init__(self, theModeIdx: Optional[int]) -> None: ...
	def Add(self, theSensitive: Select3D_SensitiveEntity) -> None: ...
	def BVHUpdateStatus(self) -> SelectMgr_TypeOfBVHUpdate: ...
	def ChangeEntities(self) -> False: ...
	def Clear(self) -> None: ...
	def Destroy(self) -> None: ...
	def Entities(self) -> False: ...
	def GetSelectionState(self) -> SelectMgr_StateOfSelection: ...
	def Init(self) -> None: ...
	def IsEmpty(self) -> bool: ...
	def Mode(self) -> int: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Sensitive(self) -> SelectMgr_SensitiveEntity: ...
	def Sensitivity(self) -> int: ...
	def SetSelectionState(self, theState: SelectMgr_StateOfSelection) -> None: ...
	def SetSensitivity(self, theNewSens: int) -> None: ...
	def UpdateBVHStatus(self, theStatus: SelectMgr_TypeOfBVHUpdate) -> None: ...
	def UpdateStatus(self) -> SelectMgr_TypeOfUpdate: ...
	def UpdateStatus(self, theStatus: SelectMgr_TypeOfUpdate) -> None: ...

class SelectMgr_SelectionManager(Standard_Transient):
	def __init__(self, theSelector: SelectMgr_ViewerSelector) -> None: ...
	def Activate(self, theObject: SelectMgr_SelectableObject, theMode: Optional[int]) -> None: ...
	def ClearSelectionStructures(self, theObj: SelectMgr_SelectableObject, theMode: Optional[int]) -> None: ...
	def Contains(self, theObject: SelectMgr_SelectableObject) -> bool: ...
	def Deactivate(self, theObject: SelectMgr_SelectableObject, theMode: Optional[int]) -> None: ...
	def IsActivated(self, theObject: SelectMgr_SelectableObject, theMode: Optional[int]) -> bool: ...
	def Load(self, theObject: SelectMgr_SelectableObject, theMode: Optional[int]) -> None: ...
	def RecomputeSelection(self, theObject: SelectMgr_SelectableObject, theIsForce: Optional[bool], theMode: Optional[int]) -> None: ...
	def Remove(self, theObject: SelectMgr_SelectableObject) -> None: ...
	def RestoreSelectionStructures(self, theObj: SelectMgr_SelectableObject, theMode: Optional[int]) -> None: ...
	def Selector(self) -> SelectMgr_ViewerSelector: ...
	def SetSelectionSensitivity(self, theObject: SelectMgr_SelectableObject, theMode: int, theNewSens: int) -> None: ...
	def SetUpdateMode(self, theObject: SelectMgr_SelectableObject, theType: SelectMgr_TypeOfUpdate) -> None: ...
	def SetUpdateMode(self, theObject: SelectMgr_SelectableObject, theMode: int, theType: SelectMgr_TypeOfUpdate) -> None: ...
	def Update(self, theObject: SelectMgr_SelectableObject, theIsForce: Optional[bool]) -> None: ...
	def UpdateSelection(self, theObj: SelectMgr_SelectableObject) -> None: ...

class SelectMgr_SensitiveEntity(Standard_Transient):
	def __init__(self, theEntity: Select3D_SensitiveEntity) -> None: ...
	def BaseSensitive(self) -> Select3D_SensitiveEntity: ...
	def Clear(self) -> None: ...
	def IsActiveForSelection(self) -> bool: ...
	def ResetSelectionActiveStatus(self) -> None: ...
	def SetActiveForSelection(self) -> None: ...

class SelectMgr_SortCriterion:
	def __init__(self) -> None: ...
	def IsGreater(self, theOther: SelectMgr_SortCriterion) -> False: ...
	def IsLower(self, theOther: SelectMgr_SortCriterion) -> False: ...

class SelectMgr_ViewClipRange:
	def __init__(self) -> None: ...
	def AddClipSubRange(self, theRange: Bnd_Range) -> None: ...
	def AddClippingPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane, thePickRay: gp_Ax1) -> None: ...
	def ChangeUnclipRange(self) -> Bnd_Range: ...
	def GetNearestDepth(self, theRange: Bnd_Range) -> Tuple[bool, float]: ...
	def IsClipped(self, theDepth: float) -> bool: ...
	def SetVoid(self) -> None: ...

class SelectMgr_CompositionFilter(SelectMgr_Filter):
	def ActsOn(self, aStandardMode: TopAbs_ShapeEnum) -> bool: ...
	def Add(self, afilter: SelectMgr_Filter) -> None: ...
	def Clear(self) -> None: ...
	def IsEmpty(self) -> bool: ...
	def IsIn(self, aFilter: SelectMgr_Filter) -> bool: ...
	def Remove(self, aFilter: SelectMgr_Filter) -> None: ...
	def StoredFilters(self) -> SelectMgr_ListOfFilter: ...

class SelectMgr_AndFilter(SelectMgr_CompositionFilter):
	def __init__(self) -> None: ...
	def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...

class SelectMgr_OrFilter(SelectMgr_CompositionFilter):
	def __init__(self) -> None: ...
	def IsOk(self, anobj: SelectMgr_EntityOwner) -> bool: ...
	def SetDisabledObjects(self, theObjects: Graphic3d_NMapOfTransient) -> None: ...
