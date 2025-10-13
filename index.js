const express = require("express");
const app = express();

const PORT = process.env.PORT || 8000;

app.get("/", (req, res) => {
  res.send({ message: "Poetic Music Backend is alive on Railway!" });
});

app.get("/health", (req, res) => {
  res.send({ status: "ok" });
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Server running on port ${PORT}`);
});