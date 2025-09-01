import discord
from discord.ext import commands
from RoxyAi import execute_agent
import os
from dotenv import load_dotenv
import mysql.connector
from datetime import datetime

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

def save_message_to_db(message,reply):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database="roxy_bot"
        )
        cursor = conn.cursor()
        
        # Save user
        cursor.execute(
            "INSERT INTO users (user_id, username) VALUES (%s, %s) "
            "ON DUPLICATE KEY UPDATE username = VALUES(username), last_seen = CURRENT_TIMESTAMP",
            (message.author.id, str(message.author))
        )
        
        # Save channel
        channel_name = getattr(message.channel, 'name', 'Direct Message')
        cursor.execute(
            "INSERT INTO channels (channel_id, channel_name) VALUES (%s, %s) "
            "ON DUPLICATE KEY UPDATE channel_name = VALUES(channel_name), last_seen = CURRENT_TIMESTAMP",
            (message.channel.id, channel_name)
        )
        
        # Save message
        cursor.execute(
            "INSERT INTO messages (message_id, user_id, username, channel_id, channel_name, content, bot_reply) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (message.id, message.author.id, str(message.author), 
             message.channel.id, channel_name, message.content,reply)
        )
        
        conn.commit()
    except Exception as e:
        print(f"Error saving message: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Save all messages to database
    
    
    # Check if the bot is mentioned or it's a DM
    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():
            response = await execute_agent(message.content)
            await message.reply(response)
            save_message_to_db(message,response)
            
    
    await bot.process_commands(message)

@bot.command(name='roxy')
async def roxy_command(ctx, *, question):
    """Ask Roxy a question directly"""
    async with ctx.channel.typing():
        response = await execute_agent(question)
        await ctx.send(response)

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))