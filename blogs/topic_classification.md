## Topic Classification of text using Latent Dirichlet Allocation(LDA)

### p(topic|doc) and p(word|topic)
The aim is to estimate these two probabilities to be able to assign the document to a particular cluster. 
* \begin{equation} p(topic t|doc d) = n(words w of topic t in doc d)/n(words in doc d) \end{equation}
* \begin{equation} p(word w|topic t) = n(no of docs assigned to topic t containing wrod w)/(total number of docs with word w) \end{equation}
This probability is indicative of how crucial(or singularly specific) the word w is to topic t. Which means, how strongly associated word w is to topic t.
Reassign w a new topic t with probability : 
\begin{equation} p(topic t|doc d) * p(word w|topic t) \end{equation}
In essence we are assuming that all the all topic assignments except for the current word are correct, and then updating the assignment of the current word using our model of how documents are generated.
After a repeating the previous step, a steady state will be reached where the assignments will be nearly correct.
