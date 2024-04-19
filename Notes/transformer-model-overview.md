## Transformer Architecture

- RNNs / LSTMs
  - A feedback loop for propagating information forward.
  - Useful for modeling sequential things like time series, language (a sequence of words).

## Encoder / Decoder Architecture

- Ditch RNNs for feed-forward neural networks (FFNNs).
- Use self-attention.
  - This makes it parallelizable.

## Self-Attention

- Each Encoder and Decoder has a list of embeddings (vectors) for each token.
- Self-Attention produces a weighted average of all token embeddings. The magic is in computing the attention weights.
- This results in tokens being tied to other tokens that are important for its context.

## Three matrices of weights are learned through the backpropagation:
- Query (Wq)
- Key (Wk)
- Value (Wv)

## Every token gets a query (q), key (k), value (v) vector by multiplying its embedding against these matrices.

- Compute a score for each token by multiplying (dot product) its query with each key.
- A mask can be applied to prevent tokens from "peeking" into future tokens (words).

- GPT does this, but BERT does something else with masked language modeling.
- Multiply values by scores and sum them up.

## Multi-Headed Self Attention

- The q, k, v vectors are reshaped into matrices.
- Then each row of the matrix can be processed in parallel.
- The number of rows are the number of "heads".

## Applications of Transformers

- GPT
  - Decoder-only — stacks of the decoder blocks.
  - Each Decoder consisting of a masked self-attention layer, and a feed-forward Neural Network.
- As an aside, BERT consists only of Encoders. T5 is an example of a model that uses both Encoder and Decoder.

**No concept of input** — all it does is generate the next token over and over.
* Use attention to maintain relationship to previous words/tokens.
* You ‘prompt’ it with tokens of your question or whatever.
* It then keeps on generating given the previous tokens.
* Getting rid of the idea of input and outputs is what allows us to train on unidirectional piles of text.

## Input Processing
- Tokenization, token encoding
- Token embedding
  - Captures semantic relationships between tokens, token similarities.
- Positional encoding
  - Captures the position of the token in the input relative to the other nearby tokens.
  - Uses an interleaved sinusoidal function.
  - So it works on any length.

## Output Processing
- The stack of decoders output a vector end.
- Multiply this with the token embeddings.
- This gives you probabilities (logits) of each token being the right next token (word) in the sequence.
- You can randomize things a bit.
