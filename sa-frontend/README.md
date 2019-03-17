## Starting the Web App Locally
` $ yarn start `

## Building the application
` $ yarn build `

## Building the container
` $ docker build -f Dockerfile -t achudh/sentiment-analysis-frontend . `

## Running the container
` $ docker run -d -p 80:80 achudh/sentiment-analysis-frontend `

## Pushing the container
` $ docker push achudh/sentiment-analysis-frontend `