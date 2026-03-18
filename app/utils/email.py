from fastapi_mail import  FastMail,MessageSchema,ConnectionConfig
from pydantic import EmailStr
from config import setting


conf = ConnectionConfig(
    MAIL_USERNAME=setting.MAIL_USERNAME,
    MAIL_PASSWORD=setting.MAIL_PASSWORD,
    MAIL_FROM="AWAIS AHMED <awaisahmed123334444@gmail.com>",
    MAIL_PORT=587,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    MAIL_SERVER="smtp.gmail.com",
    USE_CREDENTIALS=True
)

async def send_verification_email(email: EmailStr, token: str):
    base = setting.BASE_URL.rstrip("/")
    verify_url = f"{base}/auth/verify-email/{token}"

    message = MessageSchema(
        subject="Verify email",
        recipients=[email],
        body=f"Click this link to verify your email: {verify_url}",
        subtype="plain",
    )

    fm = FastMail(conf)
    await fm.send_message(message)
