from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause",
            description=f"pause the current playing stream on videochat.",
            thumb_url="https://telegra.ph//file/d67a0e10e3f1c69e0c4df.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume",
            description=f"resume the paused stream on videochat.",
            thumb_url="https://telegra.ph//file/d67a0e10e3f1c69e0c4df.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Skip",
            description=f"skip the current playing stream on videochat and moves to the next stream.",
            thumb_url="https://telegra.ph//file/d67a0e10e3f1c69e0c4df.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End",
            description="end the current playing stream on videochat.",
            thumb_url="https://telegra.ph//file/d67a0e10e3f1c69e0c4df.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Shuffle",
            description="shuffle the queued songs in playlist.",
            thumb_url="https://telegra.ph//file/d67a0e10e3f1c69e0c4df.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Loop",
            description="loop the current playing track on videochat.",
            thumb_url="https://telegra.ph//file/d67a0e10e3f1c69e0c4df.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
