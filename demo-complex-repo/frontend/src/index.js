import { cfg } from './config';
// JWT-ish test string that should be rejected (bad structure)
const maybeJwt = "eyJhbGciOiJIUzI1NiJ9.invalid_payload.invalid_sig";
console.log("frontend ready", cfg, maybeJwt);
