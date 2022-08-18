FROM node:latest

WORKDIR /
COPY ./public ./public
COPY ./src ./src 
COPY ./tsconfig.json .

COPY package.json .
RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
