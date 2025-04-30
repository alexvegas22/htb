FROM node:latest as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
ENV VITE_API_URL=https://api.htb.v34l.com
ENV VITE_WEBSOCKET_URL=ws://ws.htb.v34l.com
RUN npm run build

FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf
