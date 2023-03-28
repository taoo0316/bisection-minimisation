function bisection(f, a, b, l)
    n = 0
    while b - a >= l
        n += 1
        c = (a + b) / 2
        if f(c) == 0
            return c, n
        elseif f(c) > 0
            b = c
        else
            a = c
        end
    end
    return (a + b) / 2, n
end

f(x) = -3 + 2*x - 5/(x^2)
a = 1
b = 4
l = 0.0001

x, n = bisection(f, a, b, l)

println("The approximate minimal point of the function is x ≈ ", round(x, digits=4))
println("The bisection method took $n iterations.")
