// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)
const { WebClient, LogLevel } = require("@slack/web-api");
const { Configuration, OpenAIApi } = require("openai");
const fs = require('fs')
var bodyParser = require('body-parser');
const app = require('express')();

// Configurations
const token = fs.readFileSync("./slack/slack.key").toString();
const PORT = 8000;
const openai_configuration = new Configuration({
  apiKey: fs.readFileSync("./openai.key").toString(),
});

var jsonParser = bodyParser.json()
const openai = new OpenAIApi(openai_configuration);

const client = new WebClient( token, { logLevel: LogLevel.DEBUG} );

/* LISENING ON PORT 8000 */
app.listen(PORT, () => {
  console.log(`App listening at http://localhost:${PORT}`);
});

/* SUCCESSFUL TEST */
app.get('/test', (req, res) => {
  console.log('Server Test');
  res.send(`OK - Server up and  Running at '${req.url}'`);
});

/* FORWARD MESSAGE TO THE EVENT */
async function event_handler(data) {
  question = data.event.text;
  const response = await openai.createCompletion("text-davinci-002", {
    prompt: "Q: " + question + "\nA: ",
    temperature: 1,
    max_tokens: 200,
    top_p: 1,
    best_of: 1,
    frequency_penalty: 0,
    presence_penalty: 0,
    stop: ["Q: ", "A: "]
  });
  caption = response.data.choices[0].text.trim();
  /* push the response back to channel using chat.postMessage */
  client.chat.postMessage({
    channel: data.event.channel,
    text: caption,
  })
}

/* https://api.slack.com/events/url_verification */
app.post('/', jsonParser, function (req, res) {
  data = req.body;
  switch (data.type) {
      case "url_verification":
        /* set up the environment */
        console.log("The challenge number is", data.challenge);
        res.status(200).json({ 'challenge': data.challenge });
        break;
      case "event_callback": 
        /* must respond with status 200 for acknowledgement */
        res.status(200).json( { 'status': 'success!' } )
        event_handler(data);
        break;
      default: 
        break;
  }
})


