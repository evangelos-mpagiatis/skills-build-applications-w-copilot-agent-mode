const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
export const API_BASE_URL = codespaceName
  ? `https://${codespaceName}-8000.app.github.dev`
  : 'http://localhost:8000';
