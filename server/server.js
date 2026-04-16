const express = require('express');
const path = require('path');
const { createProxyMiddleware } = require('http-proxy-middleware');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3001;
const PYTHON_API_URL = process.env.PYTHON_API_URL || 'http://localhost:8000';

// Proxy all /api requests to the Python FastAPI backend
app.use(
  '/api',
  createProxyMiddleware({
    target: PYTHON_API_URL,
    changeOrigin: true,
    onError: (err, req, res) => {
      console.error('Proxy error:', err.message);
      res.status(503).json({
        error: 'BearBot AI backend is temporarily unavailable. Please try again shortly.',
      });
    },
  })
);

// Serve the React production build
const distPath = path.join(__dirname, '..', 'client', 'dist');
app.use(express.static(distPath));

// SPA fallback — serve index.html for all non-API routes
app.get('*', (req, res) => {
  res.sendFile(path.join(distPath, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`BearBot Node.js server running on port ${PORT}`);
  console.log(`Proxying /api requests to Python backend: ${PYTHON_API_URL}`);
});
