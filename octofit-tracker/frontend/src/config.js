const codespace = process.env.REACT_APP_CODESPACE_NAME;
const API_BASE_URL = codespace
  ? `https://${codespace}-8000.app.github.dev`
  : 'http://localhost:8000';

export default API_BASE_URL;
