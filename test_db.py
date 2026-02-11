"""Script para probar la conexión a la base de datos"""
from app.core.config import settings
from app.db.database import engine
from sqlalchemy import text

print(f"🔍 Probando conexión a: {settings.DATABASE_URL}")
print("-" * 50)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Conexión exitosa!")
        print(f"   Base de datos: {settings.DATABASE_URL.split('/')[-1]}")
        print(f"   Motor: {engine.dialect.name}")
except Exception as e:
    print(f"❌ Error de conexión: {e}")
    print("\n💡 Soluciones:")
    if "postgresql" in settings.DATABASE_URL:
        print("   1. Verifica que PostgreSQL esté corriendo")
        print("   2. Verifica usuario, password y puerto en .env")
        print("   3. O cambia a SQLite: DATABASE_URL=sqlite:///./reservas.db")
    else:
        print("   Revisa tu DATABASE_URL en el archivo .env")
