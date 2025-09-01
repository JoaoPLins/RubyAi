from pydantic import BaseModel, Field
from typing import Optional, Type, ClassVar, List, Dict
from langchain.tools import BaseTool
import mysql.connector
from datetime import datetime, timedelta
import os

class ToolInputA(BaseModel):
    file_path: str = Field(default="roxy_memories.txt", description="Path to Roxy's memory file")

class ToolInputB(BaseModel):
    file_path: str = Field(default="roxy_memories_B.txt", description="Path to Roxy's memory file")

class ToolInputC(BaseModel):
    file_path: str = Field(default="roxy_memories_C.txt", description="Path to Roxy's Points of view in the novel")

class ToolInputD(BaseModel):
    file_path: str = Field(default="RoxyMTpov.txt", description="Path to Roxy's Points of view in the novel")

class ToolInputE(BaseModel):
    file_path: str = Field(default="RoxyMTpov_tultoringRudy.txt", description="Path to Roxy's point where she is tultoring Rudy")

class ToolInputF(BaseModel):
    file_path: str = Field(default="RoxyMTpov_shirone.txt", description="Path to Roxy's point where she is tultoring Pax, and exchanged leters with Rudy")

class ToolInputG(BaseModel):
    file_path: str = Field(default="RoxyMTpov_searchingfortheGreyrats.txt", description="Path to Roxy's point where she is searching for Rudy and zenith")

class ToolInputH(BaseModel):
    file_path: str = Field(default="RoxyMTpov_Labyrinth.txt", description="Path to Roxy's point where she is trying to save zenith and end starts having romantic feelings for Rudy")

class ToolInputI(BaseModel):
    file_path: str = Field(default="RoxyMTpov_first_years_withRudy.txt", description="Path to Roxy's point where she is starting her life as Rudy's second wife")

class ReadCoreMemoriesToolA(BaseTool):
    name: ClassVar[str] = "read_roxy_memoriesA"
    description: ClassVar[str] = "Accesses Roxy Migurdia's core memories when needed for context for things before meeting Rudy"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputA
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "roxy_memories.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Roxy remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "roxy_memories.txt") -> str:
        return self._run(file_path)

class ReadCoreMemoriesToolB(BaseTool):
    name: ClassVar[str] = "read_roxy_memoriesB"
    description: ClassVar[str] = "Accesses Roxy Migurdia's core memories when needed for context for from the moment you met Rudy up to how you ended up with him"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputB
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "roxy_memories_B.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Roxy remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "roxy_memories_B.txt") -> str:
        return self._run(file_path)


class ReadCoreMemoriesToolC(BaseTool):
    name: ClassVar[str] = "read_roxy_memoriesC"
    description: ClassVar[str] = "Accesses Roxy Migurdia's core memories when needed for context for from after you married Rudy and present"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputC
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "roxy_memories_C.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Roxy remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "roxy_memories_C.txt") -> str:
        return self._run(file_path)

class ReadnovelpovstultoringRudy(BaseTool):
    name: ClassVar[str] = "Read_novel_povs_tultoringRudy"
    description: ClassVar[str] = "Accesses the novel parts where Roxy is tultoring Rudy"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputE
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "RoxyMTpov_tultoringRudy.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Roxy remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "RoxyMTpov_tultoringRudy.txt") -> str:
        return self._run(file_path)

class Readnovelpovshirone(BaseTool):
    name: ClassVar[str] = "read_novel_RoxyMTpov_shirone"
    description: ClassVar[str] = "Accesses the novel parts where Roxy is tultoring Pax, and exchanged leters with Rudy"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputF
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "RoxyMTpov_shirone.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Roxy remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "RoxyMTpov_shirone.txt") -> str:
        return self._run(file_path)

class ReadnovelpovGreyratSearch(BaseTool):
    name: ClassVar[str] = "read_novel_RoxyMTpov_greyrat_search"
    description: ClassVar[str] = "Accesses the novel parts where Roxy is searching for Rudy and zenith"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputG
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "RoxyMTpov_searchingfortheGreyrats.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Roxy remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "RoxyMTpov_searchingfortheGreyrats.txt") -> str:
        return self._run(file_path)

class ReadnovelpovLabyritnth(BaseTool):
    name: ClassVar[str] = "read_novel_RoxyMTpov_Labyrinth"
    description: ClassVar[str] = "Accesses the novel parts where Roxy is  trying to save zenith and end starts having romantic feelings for Rudy"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputH
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "RoxyMTpov_Labyrinth.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Roxy remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "RoxyMTpov_Labyrinth.txt") -> str:
        return self._run(file_path)

class ReadnovelpovFirstYearsWithRudy(BaseTool):
    name: ClassVar[str] = "read_novel_RoxyMTpov_first_years_withRudy"
    description: ClassVar[str] = "Accesses the novel parts where Roxy is starting her life as Rudy's second wife"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputI
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "RoxyMTpov_first_years_withRudy.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Roxy remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "RoxyMTpov_first_years_withRudy.txt") -> str:
        return self._run(file_path)

class Readnovelpovs(BaseTool):
    name: ClassVar[str] = "read_roxy_povs"
    description: ClassVar[str] = "Accesses Roxy Migurdia's moments written and most of the moments of the novel"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputC
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "RoxyMTpov.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Roxy remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "RoxyMTpov.txt") -> str:
        return self._run(file_path)

class GetPastMessagesTool(BaseTool):
    name: ClassVar[str] = "get_past_messages"
    description: ClassVar[str] = "Retrieves past conversation history from Discord"
    return_direct: ClassVar[bool] = False

    def _run(self, user_id: Optional[int] = None, channel_id: Optional[int] = None, limit: int = 5) -> str:
        """Get past messages from database"""
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database="roxy_bot"
            )
            cursor = conn.cursor(dictionary=True)
            
            query = "SELECT username, content, bot_reply, created_at FROM messages"
            conditions = []
            params = []
            
            if user_id:
                conditions.append("user_id = %s")
                params.append(user_id)
            if channel_id:
                conditions.append("channel_id = %s")
                params.append(channel_id)
                
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
                
            query += " ORDER BY created_at DESC LIMIT %s"
            params.append(limit)
            
            cursor.execute(query, params)
            messages = cursor.fetchall()
            
            if not messages:
                return "No past messages found."
                
            result = ["Past messages:"]
            for msg in messages:
                result.append(
                    f"{msg['username']} ({msg['created_at'].strftime('%Y-%m-%d %H:%M')}): "
                    f"{msg['content']}" f"{' Reply: '}" f"{msg['bot_reply']}"
                )
            
            return "\n".join(result)
            
        except Exception as e:
            return f"*can't read chat history* {str(e)}"
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    async def _arun(self, user_id: Optional[int] = None, channel_id: Optional[int] = None, limit: int = 15) -> str:
        return self._run(user_id, channel_id, limit)