document.getElementById("loginForm").onsubmit = async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const response = await fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const result = await response.json();
  if (result.success) {
  localStorage.setItem("token", result.token);
  localStorage.setItem("username", username);
  window.location.href = result.redirect;
}
 else {
    document.getElementById("message").innerText = result.message;
  }
};
