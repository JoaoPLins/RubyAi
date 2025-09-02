from pydantic import BaseModel, Field
from typing import Optional, Type, ClassVar, List, Dict
from langchain.tools import BaseTool
import mysql.connector
from datetime import datetime, timedelta
import os

class ToolInputA(BaseModel):
    file_path: str = Field(default="ruby_memories.txt", description="Path to Ruby's memory file")



class ReadCoreMemoriesTool(BaseTool):
    name: ClassVar[str] = "Ruby_roxy_memories"
    description: ClassVar[str] = "Accesses Ruby Migurdia's core memories when needed for context for things before meeting Rudy"
    args_schema: ClassVar[Type[BaseModel]] = ToolInputA
    return_direct: ClassVar[bool] = False

    def _run(self, file_path: str = "ruby_memories.txt") -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"Ruby remembers: {file.read()}"
        except Exception as e:
            return f"*Cannot acces my memory* {str(e)}"

    async def _arun(self, file_path: str = "roxy_memories.txt") -> str:
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