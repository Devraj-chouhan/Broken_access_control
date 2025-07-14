document.getElementById("loginForm").onsubmit = async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const response = await fetch("https://broken-access-control.onrender.com/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const result = await response.json();
  if (result.success) {
    localStorage.setItem("token", result.token);
    localStorage.setItem("username", username);
    window.location.href = result.redirect;
  } else {
    document.getElementById("message").innerText = result.message;
  }
};
