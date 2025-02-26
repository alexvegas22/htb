FROM node:latest 
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
ENV WEBSOCKET_PORT=8990
EXPOSE 8990
CMD ["node", "index.js"]

