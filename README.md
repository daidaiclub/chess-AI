# Chess AI

stockfish + flask

## Usage

```bash
$ pip install -r requirements.txt
$ flask run
```

--port = 5000

## API

### Get Best Move

`POST /ai`

form-data: fen
response: [best move]
