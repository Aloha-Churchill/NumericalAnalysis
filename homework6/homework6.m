
function Main()
    V = create_vandermonde(7)
end

function result = f_eval(x)
    result = 1/(1 + (10*x)^2);
end

% create vandermonde matrix

function c = create_vandermonde(N)
    h = 2/(N-1);
    x = ones(1, N);
    y = ones(1, N);
    for i = 1:N
        x(i) = -1 + (i-1)*h;
        y(i) = f_eval(x(i));
    end

    %plot interpolation points and function values
    plot(x, y, 'o')

    hold on

    V = (vander(x))

    c = V\transpose(y)
    t = linspace(-1, 1, 1001);
    plot(t, polyval(c, t));  % where a is coefficients of a polynomial

    hold off

end

