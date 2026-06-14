# KubeCart runtime status

Date: 2026-06-14

## Verified working endpoints
- Gateway: http://127.0.0.1:9000/
- Product service: http://127.0.0.1:8001/products
- Chatbot service: http://127.0.0.1:8005/chat
- Gateway proxy for products: http://127.0.0.1:9000/products
- Gateway proxy for chat: http://127.0.0.1:9000/chat

## Verification evidence
- `Invoke-WebRequest http://127.0.0.1:8001/products` returned HTTP 200 with `[]`
- `Invoke-WebRequest http://127.0.0.1:8005/chat` returned HTTP 200 with the chatbot recommendation payload
- `Invoke-WebRequest http://127.0.0.1:9000/products` returned HTTP 200 with `[]`
- `Invoke-WebRequest http://127.0.0.1:9000/chat` returned HTTP 200 with the same chatbot response
- `npm run build` in frontend completed successfully

## Notes
- The app is working at the runtime/gateway level.
- Product/order/review lists may appear empty until sample data is inserted into the database.
- The frontend should use the gateway on port 9000 rather than direct service ports.
