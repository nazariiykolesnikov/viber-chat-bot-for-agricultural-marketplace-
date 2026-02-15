from flask import Flask, request, render_template_string, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

DATABASE_URL = "postgresql://username:password@localhost:5432/agricultural_marketplace"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind = engine)

class ApplicationModel(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key = True, index = True)
    source = Column(String, nullable = False)
    message = Column(Text, nullable = False)

Base.metadata.create_all(bind = engine)

def save_application(source, message):
    session = SessionLocal()
    app_entry = ApplicationModel(source = source, message = message)
    session.add(app_entry)
    session.commit()
    session.close()

@app.route("/admin/applications", methods = ["GET", "POST"])
def admin_applications():
    session = SessionLocal()

    if request.method == "POST":
        source = request.form.get("source", "admin")
        message = request.form.get("message", "")

        if message.strip():
            save_application(source, message)
        return redirect(url_for("admin_applications"))

    apps = session.query(ApplicationModel).all()
    session.close()

    html_template = """ 
        <!DOCTYPE html> 
        <html> 
        <head> 
            <title>
                Адмін‑панель для прийому заявок від користувачів маркетплейсу
            </title>
            <style> 
                body { 
                    font-family: Arial, 
                    sans-serif; margin: 20px; 
                }
                
                table { 
                    border-collapse: collapse;
                    width: 100%; 
                    margin-top: 20px; 
                }
                     
                th, td { 
                    border: 1px solid #ddd;
                    padding: 8px; 
                }
                 
                th { 
                    background-color: #4CAF50; 
                    color: white; 
                }
                
                tr:nth-child(even) { 
                    background-color: #f2f2f2;
                }
                
                form { 
                    margin-bottom: 20px; 
                }
                
                input, textarea { 
                    padding: 8px; 
                    margin: 5px 0; 
                    width: 100%; 
                }
                
                button { 
                    background-color: #4CAF50; 
                    color: white; 
                    padding: 10px; 
                    border: none; 
                    cursor: pointer; 
                }
                
                button:hover {
                    background-color: #45a049; 
                }
            </style>
        </head>
        <body>
            <h2>Список заявок</h2>
            <form method="POST">
                <label for="source">Джерело:</label>
                <input type="text" id="source" name="source" placeholder="web / telegram / viber / admin" required>
                <label for="message">Повідомлення:</label>
                <textarea id="message" name="message" rows="3" required></textarea>
                <button type="submit">Додати заявку</button>
            </form>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Джерело</th>
                    <th>Повідомлення</th>
                </tr>
                {% for app in apps %}
                    <tr>
                        <td>{{ app.id }}</td>
                        <td>{{ app.source }}</td> 
                        <td>{{ app.message }}</td> 
                    </tr>
                {% endfor %} 
            </table>
        </body>
        </html> 
    """
    return render_template_string(html_template, apps = apps)

if __name__ == "__main__":
    print("🌐 Адмін‑панель доступна за адресою: http://localhost:5000/admin/applications")
    app.run(port = 5000, debug = True)
