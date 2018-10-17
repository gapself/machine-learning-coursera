function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly
p = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================

[m,n]=size(X)

X = [ones(m, 1) X]; #5000x401 +1 extra bias unit!!
a1=X
z2=(Theta1*a1')'           #25x401 X (5000x401)' = 25x5000'=5000x25
a2=[ones(m,1) sigmoid(z2)] #+1 extra bias unit!!
z3=a2*Theta2'      #5000x26
a3=sigmoid(z3)

[max_val, index]= max(a3,[],2)
p=index






% =========================================================================


end