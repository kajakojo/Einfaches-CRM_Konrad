from app import create_app

app = create_app()

if __name__ == '__main__':
    print("=" * 60)
    print("CRM Application Starting...")
    print("=" * 60)
    print(f"Visit: http://127.0.0.1:5000")
    print("Press CTRL+C to stop")
    print("=" * 60)
    app.run(debug=True, host='127.0.0.1', port=5000)
