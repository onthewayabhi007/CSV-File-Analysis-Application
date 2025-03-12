from pydantic import BaseModel
from typing import Optional, List

class CSVFile(BaseModel):
    file_path: str

class QueryRequest(BaseModel):
    question: str
    data_preview: Optional[str] = None

class PlotRequest(BaseModel):
    feature_x: str
    feature_y: str
    graph_type: str

class EDAResponse(BaseModel):
    summary: str

class LLMResponse(BaseModel):
    answer: str

class PlotResponse(BaseModel):
    plot_path: str