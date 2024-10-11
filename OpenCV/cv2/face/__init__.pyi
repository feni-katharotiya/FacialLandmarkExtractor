__all__: list[str] = []

import cv2
import cv2.typing
import typing as _typing


# Classes
class FaceRecognizer(cv2.Algorithm):
    # Functions
    @_typing.overload
    def train(self, src: _typing.Sequence[cv2.typing.MatLike], labels: cv2.typing.MatLike) -> None: ...
    @_typing.overload
    def train(self, src: _typing.Sequence[cv2.UMat], labels: cv2.UMat) -> None: ...

    @_typing.overload
    def update(self, src: _typing.Sequence[cv2.typing.MatLike], labels: cv2.typing.MatLike) -> None: ...
    @_typing.overload
    def update(self, src: _typing.Sequence[cv2.UMat], labels: cv2.UMat) -> None: ...

    @_typing.overload
    def predict_label(self, src: cv2.typing.MatLike) -> int: ...
    @_typing.overload
    def predict_label(self, src: cv2.UMat) -> int: ...

    @_typing.overload
    def predict(self, src: cv2.typing.MatLike) -> tuple[int, float]: ...
    @_typing.overload
    def predict(self, src: cv2.UMat) -> tuple[int, float]: ...

    @_typing.overload
    def predict_collect(self, src: cv2.typing.MatLike, collector: PredictCollector) -> None: ...
    @_typing.overload
    def predict_collect(self, src: cv2.UMat, collector: PredictCollector) -> None: ...

    def write(self, filename: str) -> None: ...

    def read(self, filename: str) -> None: ...

    def setLabelInfo(self, label: int, strInfo: str) -> None: ...

    def getLabelInfo(self, label: int) -> str: ...

    def getLabelsByString(self, str: str) -> _typing.Sequence[int]: ...


class BIF(cv2.Algorithm):
    # Functions
    def getNumBands(self) -> int: ...

    def getNumRotations(self) -> int: ...

    @_typing.overload
    def compute(self, image: cv2.typing.MatLike, features: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def compute(self, image: cv2.UMat, features: cv2.UMat | None = ...) -> cv2.UMat: ...

    @classmethod
    def create(cls, num_bands: int = ..., num_rotations: int = ...) -> BIF: ...


class FacemarkKazemi(Facemark):
    ...

class Facemark(cv2.Algorithm):
    # Functions
    def loadModel(self, model: str) -> None: ...

    @_typing.overload
    def fit(self, image: cv2.typing.MatLike, faces: cv2.typing.MatLike, landmarks: _typing.Sequence[cv2.typing.MatLike] | None = ...) -> tuple[bool, _typing.Sequence[cv2.typing.MatLike]]: ...
    @_typing.overload
    def fit(self, image: cv2.UMat, faces: cv2.UMat, landmarks: _typing.Sequence[cv2.UMat] | None = ...) -> tuple[bool, _typing.Sequence[cv2.UMat]]: ...


class FacemarkAAM(FacemarkTrain):
    ...

class FacemarkTrain(Facemark):
    ...

class FacemarkLBF(FacemarkTrain):
    ...

class BasicFaceRecognizer(FaceRecognizer):
    # Functions
    def getNumComponents(self) -> int: ...

    def setNumComponents(self, val: int) -> None: ...

    def getThreshold(self) -> float: ...

    def setThreshold(self, val: float) -> None: ...

    def getProjections(self) -> _typing.Sequence[cv2.typing.MatLike]: ...

    def getLabels(self) -> cv2.typing.MatLike: ...

    def getEigenValues(self) -> cv2.typing.MatLike: ...

    def getEigenVectors(self) -> cv2.typing.MatLike: ...

    def getMean(self) -> cv2.typing.MatLike: ...


class EigenFaceRecognizer(BasicFaceRecognizer):
    # Functions
    @classmethod
    def create(cls, num_components: int = ..., threshold: float = ...) -> EigenFaceRecognizer: ...


class FisherFaceRecognizer(BasicFaceRecognizer):
    # Functions
    @classmethod
    def create(cls, num_components: int = ..., threshold: float = ...) -> FisherFaceRecognizer: ...


class LBPHFaceRecognizer(FaceRecognizer):
    # Functions
    def getGridX(self) -> int: ...

    def setGridX(self, val: int) -> None: ...

    def getGridY(self) -> int: ...

    def setGridY(self, val: int) -> None: ...

    def getRadius(self) -> int: ...

    def setRadius(self, val: int) -> None: ...

    def getNeighbors(self) -> int: ...

    def setNeighbors(self, val: int) -> None: ...

    def getThreshold(self) -> float: ...

    def setThreshold(self, val: float) -> None: ...

    def getHistograms(self) -> _typing.Sequence[cv2.typing.MatLike]: ...

    def getLabels(self) -> cv2.typing.MatLike: ...

    @classmethod
    def create(cls, radius: int = ..., neighbors: int = ..., grid_x: int = ..., grid_y: int = ..., threshold: float = ...) -> LBPHFaceRecognizer: ...


class MACE(cv2.Algorithm):
    # Functions
    def salt(self, passphrase: str) -> None: ...

    @_typing.overload
    def train(self, images: _typing.Sequence[cv2.typing.MatLike]) -> None: ...
    @_typing.overload
    def train(self, images: _typing.Sequence[cv2.UMat]) -> None: ...

    @_typing.overload
    def same(self, query: cv2.typing.MatLike) -> bool: ...
    @_typing.overload
    def same(self, query: cv2.UMat) -> bool: ...

    @classmethod
    def load(cls, filename: str, objname: str = ...) -> MACE: ...

    @classmethod
    def create(cls, IMGSIZE: int = ...) -> MACE: ...


class PredictCollector:
    ...

class StandardCollector(PredictCollector):
    # Functions
    def getMinLabel(self) -> int: ...

    def getMinDist(self) -> float: ...

    def getResults(self, sorted: bool = ...) -> _typing.Sequence[tuple[int, float]]: ...

    @classmethod
    def create(cls, threshold: float = ...) -> StandardCollector: ...



# Functions
def createFacemarkAAM() -> Facemark: ...

def createFacemarkKazemi() -> Facemark: ...

def createFacemarkLBF() -> Facemark: ...

@_typing.overload
def drawFacemarks(image: cv2.typing.MatLike, points: cv2.typing.MatLike, color: cv2.typing.Scalar = ...) -> cv2.typing.MatLike: ...
@_typing.overload
def drawFacemarks(image: cv2.UMat, points: cv2.UMat, color: cv2.typing.Scalar = ...) -> cv2.UMat: ...

@_typing.overload
def getFacesHAAR(image: cv2.typing.MatLike, face_cascade_name: str, faces: cv2.typing.MatLike | None = ...) -> tuple[bool, cv2.typing.MatLike]: ...
@_typing.overload
def getFacesHAAR(image: cv2.UMat, face_cascade_name: str, faces: cv2.UMat | None = ...) -> tuple[bool, cv2.UMat]: ...

def loadDatasetList(imageList: str, annotationList: str, images: _typing.Sequence[str], annotations: _typing.Sequence[str]) -> bool: ...

@_typing.overload
def loadFacePoints(filename: str, points: cv2.typing.MatLike | None = ..., offset: float = ...) -> tuple[bool, cv2.typing.MatLike]: ...
@_typing.overload
def loadFacePoints(filename: str, points: cv2.UMat | None = ..., offset: float = ...) -> tuple[bool, cv2.UMat]: ...

@_typing.overload
def loadTrainingData(filename: str, images: _typing.Sequence[str], facePoints: cv2.typing.MatLike | None = ..., delim: str = ..., offset: float = ...) -> tuple[bool, cv2.typing.MatLike]: ...
@_typing.overload
def loadTrainingData(filename: str, images: _typing.Sequence[str], facePoints: cv2.UMat | None = ..., delim: str = ..., offset: float = ...) -> tuple[bool, cv2.UMat]: ...
@_typing.overload
def loadTrainingData(imageList: str, groundTruth: str, images: _typing.Sequence[str], facePoints: cv2.typing.MatLike | None = ..., offset: float = ...) -> tuple[bool, cv2.typing.MatLike]: ...
@_typing.overload
def loadTrainingData(imageList: str, groundTruth: str, images: _typing.Sequence[str], facePoints: cv2.UMat | None = ..., offset: float = ...) -> tuple[bool, cv2.UMat]: ...
@_typing.overload
def loadTrainingData(filename: _typing.Sequence[str], trainlandmarks: _typing.Sequence[_typing.Sequence[cv2.typing.Point2f]], trainimages: _typing.Sequence[str]) -> bool: ...


