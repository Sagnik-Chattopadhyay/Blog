<style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1, h2 {
            color: #2c3e50;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-left: 3px solid #2c3e50;
            overflow-x: auto;
        }
        code {
            font-family: Consolas, monospace;
        }
    </style>
</head>
<body>
    <h1>Blog Website Using Django</h1>
    <p>This is a fully functional blog website built using the Django framework. The project allows users to create and read blog posts. It demonstrates Django's capabilities in building dynamic and robust web applications with minimal configuration.</p>
    
    <h2>Features</h2>
    <ul>
        <li><strong>User Authentication:</strong> Secure login and registration functionality.</li>
        <li><strong>Blog Management:</strong>
            <ul>
                <li>Users can create and view blog posts.</li>
                <li>Blog posts are displayed dynamically with pagination for easy navigation.</li>
            </ul>
        </li>
    </ul>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Backend:</strong> Django Framework (Python)</li>
        <li><strong>Frontend:</strong> HTML, CSS</li>
        <li><strong>Database:</strong> SQLite</li>
    </ul>

    <h2>Installation and Setup</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone &lt;repository-url&gt;
cd &lt;repository-directory&gt;</code></pre>
        </li>
        <li>Create a virtual environment and activate it:
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Apply database migrations:
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li>Run the development server:
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li>Open your browser and navigate to <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>.</li>
    </ol>

    <h2>Usage</h2>
    <ul>
        <li>Register as a user and log in to create blog posts.</li>
        <li>Browse through existing posts on the homepage.</li>
    </ul>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to fork the repository and submit pull requests.</p>

    <h2>License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>
</body>