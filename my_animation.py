from manim import *

class MyFirstScene(Scene):
    def construct(self):
        plane = ComplexPlane().scale(1.5)
        self.play(Create(plane))
        text = Text("Hello, and welcome to this video on Euler's Identity,\n"
        "where will will bring together the worlds of algebra,\n"
        "trigonometry and complex analysis!", font_size=40, color=YELLOW).to_edge(UP).shift(DOWN*1)
       
        self.play(Write(text))
        self.wait(3)


class EulersIdentity(Scene):
    def construct(self):
        # Display Euler's Identity
        equation = MathTex("e^{i\pi} + 1 = 0", font_size=60, color=BLUE)
        equation.to_edge(UP)

        # Display question
        question1 = Text("What is this mysterious equation?", font_size=35)
        question1.next_to(equation, DOWN, buff=1.25)
        
        question2 = Text("What is e? and how can you raise it to an imaginary number?", font_size=35)
        question2.next_to(question1, DOWN, buff=1.25)

        question3 = Text("What is an imaginary number?", font_size=35)
        question3.next_to(question2, DOWN, buff=1.25)

        # Animations
        self.play(Write(equation))
        
        self.wait(2)

        self.play(FadeIn(question1))

        self.wait(2)

        self.play(FadeIn(question2))

        self.wait(2)

        self.play(FadeIn(question3))
        self.wait(3)

class EulersHook(Scene):
    def construct(self):
        # complex plane
        plane = ComplexPlane().scale(1.5)
        self.play(Create(plane))

        # unit circle
        circle = Circle(radius=1.5).set_color(WHITE)
        self.play(Create(circle))
        self.wait(1)

        # Function to get moving point
        def moving_point(t):
            return np.exp(1j * TAU * t)

        dot = Dot(plane.number_to_point(moving_point(0)), color=RED)
        line = Line(plane.c2p(0,0), dot.get_center(), color=RED)
        label = MathTex("e^{i\\theta}").next_to(dot, RIGHT, buff=0.2)
        
        self.add(dot, line, label)

        text = MathTex(r"\text{How is it that } e, \pi, \text{and imaginary numbers are so deeply connected?}", font_size=50).scale(0.8).move_to(UP * 2.5)
        text1 = Text("Let's first explore the realm of complex numbers", font_size=40).move_to(DOWN*2.5)

        self.play(Write(text))

        def update_dot(mob, alpha):
            theta = interpolate(0, TAU, alpha)
            z_value = moving_point(theta)
            point = plane.number_to_point(z_value)
            mob.move_to(point)
            line.become(Line(plane.c2p(0,0), point, color=RED))
            label.next_to(dot, RIGHT, buff=0.2)

        self.play(UpdateFromAlphaFunc(dot, update_dot), run_time=5)
        
        self.play(Write(text1))
        self.wait(1.5)



        


class ComplexIntro(Scene):
    def construct(self):
        # cartesian form of complex equation
        statement = Text('Complex Numbers', font_size=35)
        statement.to_edge(UP)
        statement1 = Text("Denoted as", font_size=30)
        statement1.next_to(statement, DOWN)
        equation = MathTex("z =", "x", "+", "y", "i",",", color=BLUE)
        equation.next_to(statement1, DOWN)
       
        symbol = MathTex(r"\mathbb{C}", font_size=60)
        symbol.next_to(statement, RIGHT)
       



        # Annotation for i
        i_annotation = MathTex(r"\text{where } i = \sqrt{-1}", font_size=30).next_to(equation, DOWN * 1)



        # Display everything
        self.play(Write(statement))
        self.play(Write(symbol))
        self.wait(1)
        self.play(FadeIn(statement1))
        self.wait(1)
        self.play(Write(equation))
        self.wait(1)
        self.play(Write(i_annotation))
        
        self.wait(3.5)

        self.play(FadeOut(statement), FadeOut(symbol), FadeOut(statement1), FadeOut(i_annotation), FadeOut(equation))

        equation_part = MathTex("z = x + yi", color=BLUE)
        text_part1 = Text("Graphically,", font_size=33)
        text_part2 = Text("represents a point on the complex plane...", font_size=33)

        
        text_part1.to_edge(UP).to_edge(LEFT)
        equation_part.next_to(text_part1, RIGHT, buff=0.25)
        text_part2.next_to(equation_part, RIGHT, buff=0.25)

        
        group = VGroup(text_part1, equation_part, text_part2)

        
        self.play(Write(group))

        # complex plane graph
        plane = ComplexPlane().scale(0.70).center().to_edge(DOWN)
        real_label = Text("Real(z)", font_size=25).next_to(plane, RIGHT)
        imag_label = Text("Imaginary(z)", font_size=25).next_to(plane, UP)
        self.play(Write(plane), Write(real_label), Write(imag_label))

        # plot  point in the first quadrant

        x_value = 4
        y_value = 3
        dot_location = plane.number_to_point(x_value + y_value * 1j)
        dot = Dot(dot_location, color=RED)
        label = MathTex("x+yi", font_size=35).next_to(dot, UR, buff=0.1)
        self.play(FadeIn(dot), Write(label))

        vertical_line = DashedLine(dot_location, plane.c2p(x_value, 0), color=WHITE)
        horizontal_line = DashedLine(dot_location, plane.c2p(0, y_value), color=WHITE)

        x_label = MathTex("x").next_to(vertical_line, DOWN, buff=0.1)
        y_label = MathTex("y").next_to(horizontal_line, LEFT, buff=0.1)

        self.play(Create(vertical_line), Create(horizontal_line), Write(x_label), Write(y_label))

        self.wait(3)

class ComplexExplanation(Scene):
    def construct(self):
        # Quadratic formula
        statement = Text("Let's look at why complex numbers need to exist", font_size=35)
        
        equation = MathTex("x^2 + x + 1 = 0", color=BLUE)
        equation.to_edge(UP)
        equation.to_edge(UP)
        equation.shift(DOWN * 1)

        self.play(Write(statement))
        self.wait(2)
        self.play(FadeOut(statement))
        self.play(Write(equation))
        
        self.wait(1)
        

        

        statement2 = Text("If we wanted to find the solutions of this quadratic equation,\n"
                  "we could plug the values of the coefficients into the quadratic formula", font_size=32)
        statement2.next_to(equation, DOWN)
        self.play(Write(statement2))
        self.wait(2.5)
        self.play(FadeOut(statement2))
        formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        formula.move_to(ORIGIN)
        self.play(Write(formula))
        self.wait(2)

        # transformed values
        substituted = MathTex(r"x = \frac{-1 \pm \sqrt{1 - 4(1)(1)}}{2(1)}")
        
        self.play(Transform(formula, substituted))
        self.wait(2)

        simplified = MathTex(r"x = \frac{-1 \pm \sqrt{-3}}{2}")
        
        self.play(Transform(formula, simplified))
        self.wait(2)
        self.play(FadeOut(equation))
        self.play(FadeOut(formula))
        simplified = MathTex(r"x = \frac{-1 \pm \sqrt{-3}}{2}", color=BLUE)
        simplified.to_edge(UP)
        self.play(Write(simplified))

        # highlight negative in square root
        numerator = Text("Take a look at the square root term in the numerator", font_size=25)
        numerator.next_to(simplified, DOWN*1.25)

        
        square_root = MathTex(r"\sqrt{-3}")
        square_root.set_color(RED)
        square_root.next_to(numerator, DOWN)
        
        self.play(Write(numerator))
        self.play(Write(square_root))
        self.wait(2)
        self.play(FadeOut(numerator))
        

        # 5. sqrt(-1) dilemma
        
        real_numbers = Text("The expression under the square root is negative, meaning the quadratic equation has no real solutions", font_size=25)
        symbol = MathTex(r"\mathbb{R}", font_size=40)
        explanation2 = MathTex(r" \sqrt{-3}")
        explanation4 = Text("is nonsense in the realm of real numbers, as no x can mulitply by itself \n"
        "to become a negative value", font_size=25)
        
        # Align
        real_numbers.to_edge(LEFT)
        explanation2.next_to(real_numbers, DOWN).align_to(real_numbers, LEFT)
        explanation4.next_to(explanation2, RIGHT, buff=0.2)
        
        
        
        self.play(Write(real_numbers))
        
        self.wait(0.5)
        self.play(Write(explanation2))
        self.play(Write(explanation4))
        self.wait(4)
        
        





class ComplexRepresentation(Scene):

    def construct(self):
        # complex number in exponential form
        statement = Text("z = x + yi, where x corresponds to Re(z), and y corresponds to Im(z) \n"
        "is just one way to graphically represent a unique complex number", font_size= 30)
        statement.to_edge(UP)

        # graph with real and imaginary axes
        plane0 = ComplexPlane().scale(0.5).center()

        plane0.next_to(statement, DOWN * 3.5)
        real_label = Text("Real(z)", font_size=25).next_to(plane0, RIGHT)
        imag_label = Text("Imaginary(z)", font_size=25).next_to(plane0, UP)
        self.play(Write(statement))
        self.play(Write(plane0), Write(real_label), Write(imag_label))

        # plot a point 
        dot_location = plane0.number_to_point(4+3j)  # Change coordinates (1+2j) as desired
        dot = Dot(dot_location, color=RED)
        label = MathTex("x+yi", font_size=35).next_to(dot, UR, buff=0.1)
        self.play(FadeIn(dot), Write(label))


        self.wait(1.5)
        self.play(FadeOut(statement,plane0,real_label,imag_label,dot,label ))
        statement1 = Text('A much more useful alternative for representing a complex number is', font_size=30)
        statement1.move_to(ORIGIN)

        formula = MathTex(r"z = re^{i\theta}, \text{ where } r \text{ is the modulus and } \theta \text{ is the argument.}")
        formula1 = MathTex(r"z = re^{i\theta")

        

        formula.next_to(statement1, DOWN)
        formula1.to_edge(UP)
        statement.next_to(formula)
 
       
        self.play(Write(statement1))
        self.play(Write(formula))
        self.wait(2)

        self.play(FadeOut(formula, statement1))
        

        # display complex plane
        plane = ComplexPlane().scale(0.8).center()
       
        real_label = Text("Re(z)", font_size=25).next_to(plane, RIGHT)
        imag_label = Text("Im(z)", font_size=25).next_to(plane, UP)

        
        
        self.play(Write(plane), Write(real_label), Write(imag_label))
        self.wait(1)

        # point on the complex plane
        point_coords = 5 * np.exp(2j * PI / 8)  # Adjust this for different modulus and argument
        dot = Dot(plane.number_to_point(point_coords), color=RED)

        dotted_line = DashedLine(dot.get_center(), [dot.get_center()[0], 0, 0], dash_length=0.1, color=WHITE)
        dotted_label = MathTex('x').next_to(dotted_line, DOWN, buff=0.1)


        # modulus like
        magnitude_line = Line(plane.c2p(0,0), dot.get_center(), color=BLUE)

        # argument angle theta
        theta_angle = np.angle(point_coords)  # Angle in radians
        arc = Arc(start_angle=0, angle=theta_angle, radius=0.5, color=GREEN)

        # theta symbol
        theta_label = MathTex(r"\theta").next_to(arc, RIGHT, buff=0.3).shift(UP * 0.2)  # Shift it upwards a bit

        # modulus label
        r_position = (magnitude_line.get_start() + magnitude_line.get_end()) / 2  # Midpoint of magnitude line
        r_label = MathTex("r").next_to(r_position, LEFT, buff=0.25)

        # display 
        self.play(FadeIn(dot), Create(magnitude_line), Create(arc))
        self.wait(1.5)
        self.play(FadeIn(theta_label), Write(r_label))
        self.wait(1)
        self.play(FadeIn(dotted_line), Write(dotted_label))
        self.wait(3)






class ComplexTriangle(Scene): ###fix pythag transformation
    def construct(self):
        # display the complex plane
        plane = ComplexPlane().scale(0.8).center()
        self.play(Create(plane))
        self.wait(1)

        # plot point on the complex plane (representing a complex number)
        point_coords = 4 * np.exp(2j * PI / 7)
        dot = Dot(plane.number_to_point(point_coords), color=RED)

        # magnitude line segment from the origin to the point (hypotenuse r)
        magnitude_line = Line(plane.c2p(0,0), dot.get_center(), color=BLUE)

        # vertical line from the dot to the x-axis (imaginary part y)
        vertical_line = Line(dot.get_center(), [dot.get_center()[0], 0, 0], color=BLUE)
        
        horizontal_line = Line(plane.c2p(0, 0), [dot.get_center()[0], 0, 0], color=WHITE)

        # angle theta
        theta = np.angle(point_coords)
        arc = Arc(start_angle=0, angle=theta, radius=0.5, color=GREEN)

        # labels for r, x, and y
        r_label = MathTex("r").next_to(magnitude_line, buff=-0.5).shift(LEFT)
        x_label = MathTex("x").next_to(vertical_line.get_end(), DOWN, buff=0.1).shift(LEFT * 0.75)
        y_label = MathTex("y").next_to(vertical_line, RIGHT, buff=0.1)
        theta_label = MathTex(r"\theta").next_to(arc, RIGHT, buff=0.1).shift(UP * 0.2)

        # display
        self.play(FadeIn(dot), Create(magnitude_line), Create(vertical_line), Create(arc), 
                  Write(r_label), Write(x_label), Write(y_label), Write(theta_label), Create(horizontal_line))
        self.wait(2)

        self.play(FadeOut(plane), FadeOut(dot))

        
        

        # transform labels into the Pythagorean theorem equation
        pythagorean = MathTex("r^2", "=", "x^2", "+", "y^2").move_to(ORIGIN)
        new_equation = MathTex("r", "=", r"\sqrt{x^2 + y^2}").move_to(ORIGIN)
        title = Text("By Pythagorean Theorem", font_size=30, color=RED)
        title.to_edge(UP)

        self.play(Write(title))
        self.play(FadeOut(magnitude_line), FadeOut(vertical_line), FadeOut(arc), FadeOut(theta_label), FadeOut(horizontal_line))
        self.play(
            Transform(r_label, pythagorean[0]),
            Transform(x_label, pythagorean[2]),
            Transform(y_label, pythagorean[4]),
            FadeIn(pythagorean[1]), FadeIn(pythagorean[3]),
        )
        
        self.wait(2)

        equation1 = MathTex(r"r^2 = x^2 + y^2 \implies r = \sqrt{x^2 + y^2}")
        equation1.move_to(ORIGIN)

        self.play(FadeOut(r_label), FadeOut(x_label), FadeOut(y_label), FadeOut(pythagorean))
        self.play(FadeIn(equation1))

        self.wait(3)

        

       
        
        
        
class TrigonometricIdentities(Scene):
    def construct(self):
        #  right-angled triangle
        triangle = Polygon([0, 0, 0], [3, 0, 0], [3, 4, 0], color=WHITE)
        triangle.shift(DOWN*1)
        
        r_label = MathTex("r").next_to(triangle.get_left(), LEFT, buff=0.1)
        r_label.shift(RIGHT*1.40)
        r_label.shift(UP*0.1)
        x_label = MathTex("x").next_to(triangle.get_bottom(), DOWN, buff=0.2)
        y_label = MathTex("y").next_to(triangle.get_right(), RIGHT, buff=0.2)

        # right-angle symbol inside the triangle
        horizontal_line = Line(triangle.get_corner(DR), triangle.get_corner(DL))
        vertical_line = Line(triangle.get_corner(DR), triangle.get_corner(UR))


        right_angle = RightAngle(line1=horizontal_line, line2=vertical_line, length=0.25)

        self.play(Create(triangle), Write(r_label), Write(x_label), Write(y_label), Write(right_angle))
        self.wait(1)

        # Pythagoras theorem and its simplified form
        pythagoras = MathTex("r^2", "=", "x^2", "+", "y^2").to_edge(UP)
        simplified = MathTex("r", "=", r"\sqrt{x^2 + y^2}").to_edge(UP)

        self.play(Write(pythagoras))
        self.wait(1)
        self.play(Transform(pythagoras, simplified))
        self.wait(1)

        #  trigonometric ratios
        cos_relation = MathTex(r"\cos(\theta)", "=", r"\frac{x}{r}", r"\implies x = r\cos(\theta)", color=GREEN).next_to(triangle, LEFT, buff=0.1)
        sin_relation = MathTex(r"\sin(\theta)", "=", r"\frac{y}{r}", r"\implies y = r\sin(\theta)", color=RED).next_to(cos_relation, DOWN, buff=0.5)

        self.play(Write(cos_relation))
        self.wait(1)
        self.play(Write(sin_relation))
        self.wait(3)
            
        self.play(FadeOut(triangle), FadeOut(r_label),  FadeOut(x_label),  FadeOut(y_label),  FadeOut(right_angle), FadeOut(pythagoras), FadeOut(cos_relation), FadeOut(sin_relation))

        cos_relation = MathTex(r"\cos(\theta)", "=", r"\frac{x}{r}", r"\implies x = r\cos(\theta)").to_edge(UP)
        sin_relation = MathTex(r"\sin(\theta)", "=", r"\frac{y}{r}", r"\implies y = r\sin(\theta)").next_to(cos_relation, DOWN, buff=0.5)

        self.play(Write(cos_relation))
        self.wait(1)
        self.play(Write(sin_relation))
        self.wait(2)

        intro_text = Text('Now we have relationships between x, y, r, cosine and sine')
        intro_text.next_to(sin_relation, DOWN)
        intro_text.scale(0.7)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))
        self.play(FadeOut(cos_relation), FadeOut(sin_relation))

        # complex number formula
        complex_formula = MathTex("z", "=", "re^{i\\theta}", "=", "x", "+", "iy").to_edge(UP)
        expression = MathTex(r"\text{Since we know }", "x",  "=" r"\cos(\theta)", r"\text{ and }", "y", "=" r"\sin(\theta)", r"\text{, then}")
        expression.next_to(complex_formula, DOWN)
        
        self.play(Write(complex_formula))
        self.wait(1)
        self.play(FadeIn(expression))
        self.wait(3)
        self.play(FadeOut(expression))

        # transform x and y to their trigonometric relationships
        new_formula = MathTex("z", "=", "re^{i\\theta}", "=", "r\\cos(\\theta)", "+", "ir\\sin(\\theta)")
        
        self.play(TransformMatchingTex(complex_formula, new_formula))
        self.wait(2)

        # Euler's Identity
        euler_identity = MathTex("e^{i\\theta}", "=", "\\cos(\\theta)", "+", "i\\sin(\\theta)")
        self.play(TransformMatchingTex(new_formula, euler_identity))
        self.wait(2)

        # box highlighting Euler's Identity
        box = SurroundingRectangle(euler_identity, color=WHITE)
        label = Text("Euler's Formula").next_to(box, UP)

        
        self.play(Create(box), Write(label))
        self.wait(2)



class Cosine(Scene):
    def construct(self):
        # set axes
        axes = Axes(
            x_range=[-3.5, 3.5], 
            y_range=[-1.5, 1.5],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(
            x_label="x",
            y_label="y"
        )

        # Graph cosine function
        graph = axes.plot(lambda x: np.cos(x), color=YELLOW)
        

        self.play(Create(axes), Write(axes_labels), Create(graph))
        self.wait(1)

        # value for theta and highlight cos(theta) and cos(-theta)
        theta_val = PI / 3
        dot1 = Dot(point=axes.c2p(theta_val, np.cos(theta_val)), color=RED)
        dot2 = Dot(point=axes.c2p(-theta_val, np.cos(-theta_val)), color=RED)

       

        # equation cos(theta) = cos(-theta)
        equation = MathTex("\\cos(\\theta)", "=", "\\cos(-\\theta)").to_edge(UP)
        self.play(FadeOut(axes_labels))
        self.play(Write(equation))
        self.play(FadeIn(dot1), FadeIn(dot2))
        self.wait(3)

class Sine(Scene):
    def construct(self):
        # set axes
        axes = Axes(
            x_range=[-3.5, 3.5], 
            y_range=[-1.5, 1.5],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(
            x_label="x",
            y_label="y"
        )

        # Graph sine function
        graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        

        self.play(Create(axes), Write(axes_labels), Create(graph))
        self.wait(1)

        # pick value for theta and highlight sin(theta) and sin(-theta)
        theta_val = PI / 3
        dot1 = Dot(point=axes.c2p(theta_val, np.sin(theta_val)), color=RED)
        dot2 = Dot(point=axes.c2p(-theta_val, -np.sin(theta_val)), color=RED)

        

        # Display equation sin(-theta) = -sin(theta)
        equation = MathTex("\\sin(-\\theta)", "=", "-\\sin(\\theta)").to_edge(UP)
        self.play(FadeOut(axes_labels))
        self.play(Write(equation))
        self.play(FadeIn(dot1), FadeIn(dot2))
        self.wait(2)

class EulerToTrig(Scene):
    def construct(self):

        # Show  cos(-theta) = cos(theta) and sin(-theta) = -sin(theta)
        statement = Text('Trigonometric Identities', font_size=30).to_edge(UP)
        cos_relationship = MathTex("\\cos(-\\theta)", "=", "\\cos(\\theta)", color=GREEN).next_to(statement, DOWN)
        sin_relationship = MathTex("\\sin(-\\theta)", "=", "-\\sin(\\theta)", color=RED).next_to(cos_relationship, DOWN)
        self.play(Write(statement))
        self.wait(1.5)
        self.play(Write(cos_relationship))
        self.play(Write(sin_relationship))
        self.wait(3)
        self.play(FadeOut(cos_relationship), FadeOut(sin_relationship), FadeOut(statement))
        cos_relationship = MathTex("\\cos(-\\theta)", "=", "\\cos(\\theta)", color=GREEN).to_edge(RIGHT).shift(UP*3.25)
        sin_relationship = MathTex("\\sin(-\\theta)", "=", "-\\sin(\\theta)", color=RED).next_to(cos_relationship, DOWN)
        self.play(FadeIn(cos_relationship), FadeIn(sin_relationship))

        
        # Euler's formula for e^(i theta) and e^(-i theta)
        eulers_formula_positive = MathTex("e^{i\\theta}", "=", "\\cos(\\theta)", "+", "i\\sin(\\theta)").to_edge(UP+LEFT*2)
        eulers_formula_negative = MathTex("e^{-i\\theta}", "=", "\\cos(-\\theta)", "+", "i\\sin(-\\theta)").next_to(eulers_formula_positive, DOWN, aligned_edge=LEFT)
        eulers_formula_negative_substituted = MathTex("e^{-i\\theta}", "=", "\\cos(\\theta)", "-", "i\\sin(\\theta)").next_to(eulers_formula_positive, DOWN, aligned_edge=LEFT)
        
        self.play(Write(eulers_formula_positive))
        self.play(Write(eulers_formula_negative))
        self.wait(2)
        self.play(Transform(eulers_formula_negative, eulers_formula_negative_substituted))
        

        # Substitute the relationships into the equation
        #eulers_formula_negative_substituted = MathTex("e^{-i\\theta}", "=", "\\cos(\\theta)", "-", "i\\sin(\\theta)").next_to(eulers_formula_negative, DOWN * 1.25, RIGHT * 0.75)
        #eulers_formula_negative = MathTex("e^{-i\\theta}", "=", "\\cos(-\\theta)", "+", "i\\sin(-\\theta)").next_to(eulers_formula_negative, DOWN * 1.25, RIGHT * 0.75)
        
        
       
        self.wait(1)

        # Add both e^(i theta) and e^(-i theta) to get 2cos(theta)
        cos_combined1 = MathTex("e^{i\\theta}", "+", "e^{-i\\theta}", "=", "\\cos(\\theta)", "+", "\\cos(\\theta)","+", "i \\sin(\\theta)", "-", "i \\sin(\\theta)", color=GREEN).move_to(ORIGIN)
        
        self.play(Write(cos_combined1))
        self.wait(2)
        

        cos_combined = MathTex("e^{i\\theta}", "+", "e^{-i\\theta}", "=", "2\\cos(\\theta)", color=GREEN)
        self.play(Transform(cos_combined1, cos_combined))
        self.wait(2)
        
        

        # Divide both sides by 2 to get expression for cos(theta)
        cos_result = MathTex("\\cos(\\theta)", "=", "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}", color=GREEN).move_to(ORIGIN)
        self.play(Transform(cos_combined1, cos_result))
        self.wait(3)
        
        self.play(FadeOut(cos_combined1))

        # subtract e^(-i theta) from e^(i theta) to get 2i sin(theta)
        sin_combined1 = MathTex("e^{i\\theta}", "-", "e^{-i\\theta}", "=", "\\cos(\\theta)", "-", "\\cos(\\theta)","+", "i \\sin(\\theta)", "-","-" "i \\sin(\\theta)", color=RED).move_to(ORIGIN)
        sin_combined = MathTex("e^{i\\theta}", "-", "e^{-i\\theta}", "=", "2i\\sin(\\theta)", color=RED).move_to(ORIGIN)
        self.play(Write(sin_combined1))
        self.wait(1)
        self.play(Transform(sin_combined1, sin_combined))
        self.wait(2)

        # Divide both sides by 2i to get expression for sin(theta)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).move_to(ORIGIN)
        
        self.play(Transform(sin_combined1, sin_result))
        self.wait(3)

        self.play(FadeOut(eulers_formula_positive), FadeOut(sin_combined1), FadeOut(eulers_formula_negative), FadeOut(cos_relationship), FadeOut(sin_relationship))
        self.wait(1)

        cos_result = MathTex("\\cos(\\theta)", "=", "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}", color=GREEN).to_edge(UP)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).next_to(cos_result, DOWN)
        statement1 = Text("We have just derived sine and cosine in terms of the exponential function,\n" 
        "                         which leads us into the fascinating topic of", font_size=30).next_to(sin_result, DOWN * 2)
        statement2 = Text("Infinite Series", font_size=40, color=BLUE).next_to(statement1, DOWN * 2)

        self.play(FadeIn(cos_result))

        self.play(FadeIn(sin_result))
        self.wait(1)

        self.play(Write(statement1))
        self.wait(1.5)
        self.play(Write(statement2))
        self.wait(2)


        


class InfiniteSeries(Scene):
    def construct(self):
        # e^x infinite series 
        statement = MathTex("e^x " r"\text{ can be written in an infinitely long string of pieces added together }" , font_size=40).to_edge(UP)
        series_text = MathTex(
            "e^x", "=", "1", "+", "x", "+", 
            r"\frac{x^2}{2!}", "+", 
            r"\frac{x^3}{3!}", "+",
            r"\frac{x^4}{4!}", "+", 
            r"\frac{x^5}{5!}", "+ \dots"
        ).scale(0.8).to_edge(UP)
        self.play(Write(statement))
        self.wait(3)
        self.play(FadeOut(statement))
        self.play(Write(series_text))

        # graph of e^x 
        axes = Axes(x_range=[-2, 2], y_range=[-3, 8], axis_config={"color": BLUE})
        axes.shift(DOWN * 0.75)
        

        graph = axes.plot(lambda x: np.exp(x), color=WHITE)
        graph_label = axes.get_graph_label(graph, label='e^x')

        self.play(
            Create(axes),
            Create(graph),
            Write(graph_label)
        )

        # graph changing as you add terms
        partial_series = [
            lambda x: 1,
            lambda x: 1 + x,
            lambda x: 1 + x + x**2/np.math.factorial(2),
            lambda x: 1 + x + x**2/np.math.factorial(2) + x**3/np.math.factorial(3),
            lambda x: 1 + x + x**2/np.math.factorial(2) + x**3/np.math.factorial(3) + x**4/np.math.factorial(4),
            lambda x: 1 + x + x**2/np.math.factorial(2) + x**3/np.math.factorial(3) + x**4/np.math.factorial(4) + x**5/np.math.factorial(5)
        ]


        self.wait(1)

        terms = [
            "1 ",
            "+ x",
            "+ \\frac{x^2}{2!}",
            "+ \\frac{x^3}{3!}",
            "+ \\frac{x^4}{4!}",
            "+ \\frac{x^5}{5!}",
        ]

        previous_partial_graph = axes.plot(partial_series[0], color=YELLOW)
        current_series = MathTex("e^x", "=", *terms[0]).move_to(UP * 3.5)
        self.play(Create(previous_partial_graph), Transform(series_text, current_series), run_time=1)
        self.wait(0.5)

        #  for each remaining partial sum, transform the previous one into the current one
        for i, partial in enumerate(partial_series[1:], start=1):
            new_partial_graph = axes.plot(partial, color=YELLOW)
            current_series = MathTex("e^x", "=", *terms[:i+1]).move_to(UP * 3).scale(0.8)
            self.play(Transform(previous_partial_graph, new_partial_graph), Transform(series_text, current_series), run_time=1)
            self.wait(0.5)

        self.wait(1)

class EulersSeries(Scene):
    def construct(self):
        # Series for e^x
        series_ex = MathTex(
            "e^x", "=", "1", "+", "x", "+", 
            r"\frac{x^2}{2!}", "+", 
            r"\frac{x^3}{3!}", "+",
            r"\frac{x^4}{4!}", "+", 
            r"\frac{x^5}{5!}", "+ \dots"
        ).to_edge(UP)
        self.play(Write(series_ex))
        self.wait(1)

        statement = MathTex(r"\text{Substituting in }", "i\\theta" r"\text{ and }" "-i\\theta" r"\text{ for }" "x", r"\text{, we get:}" , font_size=35).next_to(series_ex, DOWN)
        self.play(Write(statement))
        self.wait(2)
        self.play(FadeOut(statement))

        # Series for e^{i\theta}
        series_itheta = MathTex(
            "e^{i\\theta}", "=", "1", "+", "i\\theta", "-", 
            r"\frac{\theta^2}{2!}", "-", 
            r"i\frac{\theta^3}{3!}", "+",
            r"\frac{\theta^4}{4!}", "+", 
            r"i\frac{\theta^5}{5!}", "+ \dots"
        ).next_to(series_ex, DOWN, buff=0.5)
        self.play(TransformMatchingTex(series_ex, series_itheta))

        self.wait(3)

        # Series for e^{-i\theta}
        series_minus_itheta = MathTex(
            "e^{-i\\theta}", "=", "1", "-", "i\\theta", "-", 
            r"\frac{\theta^2}{2!}", "+", 
            r"i\frac{\theta^3}{3!}", "+",
            r"\frac{\theta^4}{4!}", "-", 
            r"i\frac{\theta^5}{5!}", "+ \dots"
        ).next_to(series_itheta, DOWN, buff=0.5)
        self.play(TransformMatchingTex(series_itheta, series_minus_itheta))
        self.wait(2)


#class EulersSeries1(Scene):
   # def construct(self):
        # Properties of i
     #   properties_i = VGroup(
     #       MathTex("i =", r"\sqrt{-1}"),
     #       MathTex("i^2 =", "-1"),
     #       MathTex("i^3 =", "-i"),
     #       MathTex("i^4 =", "1"),
      #      Text("...", font_size=36)
      #  ).arrange(DOWN, buff=0.5).to_edge(UP)

     #   self.play(Write(properties_i))
      #  self.wait(2)
      #  self.play(FadeOut(properties_i))

        # Series for e^x
       # series_ex = MathTex(
      #      "e^x", "=", "1", "+", "x", "+", 
       #     r"\frac{x^2}{2!}", "+", 
      #      r"\frac{x^3}{3!}", "+",
       #     r"\frac{x^4}{4!}", "+", 
      #      r"\frac{x^5}{5!}", "+ \dots"
     #   ).to_edge(UP)
     #   self.play(Write(series_ex))
     #   self.wait(1)

        # Series for e^{i\theta}
     #   series_itheta = MathTex(
     #       "e^{i\\theta}", "=", "1", "+", "i\\theta", "-", 
     #       r"\frac{\theta^2}{2!}", "-", 
     #       r"i\frac{\theta^3}{3!}", "+",
     #       r"\frac{\theta^4}{4!}", "+", 
     #       r"i\frac{\theta^5}{5!}", "+ \dots"
     #   ).next_to(series_ex, DOWN, buff=0.5)
     #   self.play(TransformMatchingTex(series_ex, series_itheta))
     #   self.wait(1)

        # Series for e^{-i\theta}
     #   series_minus_itheta = MathTex(
     #       "e^{-i\\theta}", "=", "1", "-", "i\\theta", "-", 
     #       r"\frac{\theta^2}{2!}", "+", 
     #       r"i\frac{\theta^3}{3!}", "+",
      #      r"\frac{\theta^4}{4!}", "-", 
      #      r"i\frac{\theta^5}{5!}", "+ \dots"
      #  ).next_to(series_itheta, DOWN, buff=0.5)
     #   self.play(TransformMatchingTex(series_itheta, series_minus_itheta))
      #  self.wait(2)

class TrigSeriesFromEulers(Scene):
    def construct(self):
        # Starting series for e^{i\theta}

        cos_result = MathTex("\\cos(\\theta)", "=", "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}", color=GREEN).move_to(ORIGIN)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).next_to(cos_result, DOWN)

        series_itheta = MathTex(
            "e^{i\\theta}", "=", "1", "+", "i\\theta", "-", 
            r"\frac{\theta^2}{2!}", "-", 
            r"i\frac{\theta^3}{3!}", "+",
            r"\frac{\theta^4}{4!}", "+", 
            r"i\frac{\theta^5}{5!}", "+ \dots"
        ).to_edge(UP)

        # Series for e^{-i\theta}
        series_minus_itheta = MathTex(
            "e^{-i\\theta}", "=", "1", "-", "i\\theta", "-", 
            r"\frac{\theta^2}{2!}", "+", 
            r"i\frac{\theta^3}{3!}", "+",
            r"\frac{\theta^4}{4!}", "-", 
            r"i\frac{\theta^5}{5!}", "+ \dots"
        ).next_to(series_itheta, DOWN, buff=0.5)

        self.play(Write(series_itheta), Write(series_minus_itheta))

        statement = Text("Since we found cosine in terms of e earlier:", font_size=25)
        statement.next_to(series_minus_itheta, DOWN)
        cos_result = MathTex("\\cos(\\theta)", "=", "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}", color=GREEN).next_to(statement, DOWN)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).next_to(cos_result, DOWN)
        statement2 = MathTex(r"\text{we can add together the infinite series for }", "e^{i\\theta}" r"\text{ and }", "e^{-i\\theta}"r"\text{ and divide by 2}", font_size=30).next_to(series_minus_itheta, DOWN)

        self.play(Write(statement))
        self.wait(2)
        self.play(Write(cos_result))
    
        self.wait(3)
        self.play(FadeOut(statement))
        self.play(FadeIn(statement2))
        self.wait(3)
        self.play(FadeOut(statement2))
        self.play(FadeOut(cos_result))
        

        cos_result2 = MathTex( "\\frac{e^{i\\theta} + e^{-i\\theta}}{2}" "=", color=GREEN).next_to(series_minus_itheta, DOWN * 1.5)
        cos_result3 = MathTex(r"=\cos(\theta) =", "1", "-", r"\frac{(\theta)^2}{2!}", "+", r"\frac{(\theta)^4}{4!}", "-", r"\frac{(\theta)^6}{6!}", "+ \dots").next_to(cos_result2, DOWN * 1.5)
        comment = MathTex(r"\text{(all of the even powers of }", "\\theta}"r"\text{)}").next_to(cos_result3, DOWN)
        self.play(Write(cos_result2))
        self.wait(1)
        self.play(Write(cos_result3))
        self.wait(1)
        self.play(Write(comment))
        self.wait(3)
        self.play(FadeOut(cos_result2), FadeOut(cos_result3), FadeOut(comment))

        statement3 = Text("and since we found sine in terms of e earlier:", font_size=25)
        sin_result = MathTex("\\sin(\\theta)", "=", "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}", color=RED).next_to(statement3, DOWN)
        statement3.next_to(series_minus_itheta, DOWN)
        statement4 = MathTex(r"\text{we can subtract the infinite series for }", "-e^{i\\theta}" r"\text{ from }", "e^{i\\theta}" r"\text{ and divide by 2i}", font_size=30).next_to(series_minus_itheta, DOWN)

        self.play(Write(statement3))
        self.wait(2)
        self.play(Write(sin_result))
        self.wait(3)
        self.play(FadeOut(statement3))
        self.play(FadeIn(statement4))
        self.wait(3)
        self.play(FadeOut(statement4))
        self.play(FadeOut(sin_result))

        sin_result2 = MathTex( "\\frac{e^{i\\theta} - e^{-i\\theta}}{2i}" "=", color=RED).next_to(series_minus_itheta, DOWN * 1.5)
        sin_result3 = MathTex(r"\sin(\theta) =", "\\theta", "-", r"\frac{(\theta)^3}{3!}", "+", r"\frac{(\theta)^5}{5!}", "+ \dots")
        sin_result3.next_to(sin_result2, DOWN * 1.5)
        comment2 = MathTex(r"\text{(all of the odd powers of }", "\\theta}"r"\text{)}").next_to(sin_result3, DOWN)

        self.play(Write(sin_result2))
        self.wait(2)
        self.play(Write(sin_result3))
        self.wait(1)
        self.play(Write(comment2))
        self.wait(3)
        self.play(FadeOut(sin_result2), FadeOut(sin_result3), FadeOut(comment2), FadeOut(series_itheta), FadeOut(series_minus_itheta))

class EulersIdentityReveal(Scene):
    def construct(self):
        # Introduction to Euler's identity
        eulers_identity = MathTex("e^{i\\pi} + 1 = 0")
        intro = Text("Behold, one of the most beautiful equations in mathematics", font_size=30)
        self.play(Write(intro))
        self.wait(1)
        self.play(FadeOut(intro))
        self.wait(1)
        

        # Derivation of Euler's identity
        # Using e^(i*theta) formula:
        eulers_formula = MathTex("e^{i\\theta} =", "\\cos(\\theta)", "+", "i\\sin(\\theta)")
        self.play(Write(eulers_formula))
        self.wait(1)
        sub = MathTex(r"\text{Substituting }", "\pi",r"\text{ in for }",  "\\theta}"r"\text{:}").next_to(eulers_formula, UP)
        self.play(Write(sub))
        self.wait(2)
        self.play(FadeOut(sub))

        # Substituting theta with pi:
        substituted = MathTex("e^{i\\pi} =", "\\cos(\\pi)", "+", "i\\sin(\\pi)")
        self.play(TransformMatchingTex(eulers_formula, substituted))
        self.wait(2)

        # Evaluating the trigonometric values:
        evaluated = MathTex("e^{i\\pi} =", "-1", "+", "0i")
        self.play(TransformMatchingTex(substituted, evaluated))
        self.wait(2)

        # Simplifying to Euler's identity:
        simplified = MathTex("e^{i\\pi} + 1 = 0")
        self.play(TransformMatchingTex(evaluated, simplified))
        self.wait(1)
        


        
        conclusion = Text("And that's Euler's Identity!", font_size=30).next_to(simplified, DOWN)
        plane = ComplexPlane().scale(1.5)
        original_plane = plane.copy()
        self.add(plane)

        # Function to perform complex transformation: dilation + rotation
        def complex_transform(mob, alpha):
            factor = 1 + 0.5*np.sin(2*PI*alpha)
            angle = 2*PI*alpha
            mob.become(original_plane.copy().rotate(angle).scale(factor))

        # Apply the transformation
        self.play(Write(conclusion))
        self.play(UpdateFromAlphaFunc(plane, complex_transform), run_time=5, rate_func=linear)
        
        
        self.play(FadeOut(conclusion, simplified))
        thanks  = Text("If you made it this far, thank you for watching !")
        thanks.to_edge(UP)
        name = Text('Nathan Foale')
        name.next_to(thanks, DOWN * 2)
        self.play(Write(thanks))
        self.wait(1)
        self.play(Write(name))




class ACPhasorVisualisation(Scene):
    def construct(self):
        # AC Signals and Sinusoids
        axes = Axes(
            x_range=[0, 2*PI],
            y_range=[-1.5,1.5],
            axis_config={"color": BLUE},
        )
        curve = axes.plot(lambda x: np.sin(x), color=YELLOW)
        curve_label = axes.get_graph_label(curve, label='Sinusoidal AC Voltage').shift(UP*2)
        text = Text("Beyond Euler's formula's aesthetic beauty, the underlying mathematics \n"
        "has many practical applications. One of the most tangible and easy to visualise \n"
        "applications is in electrical engineering dealing with alternating current circuits", color=YELLOW, font_size=30)

        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))

        self.play(Create(axes), Create(curve), Write(curve_label))
        self.wait(1)

        # transition to Phasor Representation
        self.play(FadeOut(curve_label))

        # phasor Visualization
        complex_plane = ComplexPlane().scale(0.8).center()
        phasor = Line(complex_plane.c2p(0,0), complex_plane.c2p(1, 0), color=YELLOW)

        def update_phasor(mob, alpha):
            mob.become(Line(complex_plane.c2p(0,0), complex_plane.number_to_point(np.exp(1j * TAU * alpha)), color=YELLOW))
        
        self.play(Transform(axes, complex_plane), Transform(curve, phasor))
        self.play(UpdateFromAlphaFunc(phasor, update_phasor), run_time=2, rate_func=linear)

        # explanation of Phasor and Euler's Identity
        explanation = Text("The rotating vector represents the AC signal in the complex plane.", font_size=24).to_edge(UP)
        euler_explanation = MathTex("e^{j\\theta} = \\cos(\\theta) + j\\sin(\\theta)").to_edge(DOWN)
        self.play(Write(explanation), Write(euler_explanation))
        self.wait(2)

        # fadeout to conclude
        self.play(FadeOut(explanation), FadeOut(euler_explanation), FadeOut(phasor))

class ACPhasorExplanation(Scene):
    def construct(self):
        
        #  complex plane
        plane = ComplexPlane().scale(0.6).to_edge(LEFT).shift(DOWN * 0.6)
        self.play(Create(plane))

        # Explanation of Phasor and Euler's Identity
        title = Text("AC Phasor Representation", font_size=32).to_edge(UP)
        explanation1 = Text("In AC circuits, voltage or current can be represented as a rotating vector (phasor).", font_size=24).next_to(title, DOWN)
        explanation2 = Text("This phasor's projection on the vertical axis gives the instantaneous value of the AC signal.", font_size=24).next_to(explanation1, DOWN)
        self.play(Write(title), Write(explanation1), Write(explanation2))
        self.wait(2)
        
        # Display phasor (rotating vector)
        phasor_start = plane.c2p(0, 0)
        phasor_end = plane.c2p(np.cos(PI / 4), np.sin(PI / 4))
        phasor = Arrow(phasor_start, phasor_end, color=YELLOW)
        self.play(GrowArrow(phasor))
        self.wait(1)

        # Show the projection of the phasor on the vertical axis (imaginary axis)
        projection_line = DashedLine(plane.c2p(0,0), plane.c2p(0, phasor.get_end()[1]), color=RED)
        self.play(Create(projection_line))
        self.wait(1)
        
        # AC waveform corresponding to the phasor
        ac_waveform = ParametricFunction(
            lambda t: plane.c2p(t-3, np.sin(t*TAU)),
            t_range=[0, 2*PI],
            color=RED
        ).next_to(plane, RIGHT, buff=0.75)
        ac_waveform_label = Text("AC Waveform", font_size=24).next_to(ac_waveform, UP)
        self.play(Create(ac_waveform), Write(ac_waveform_label))
        self.wait(2)

        # Animation of phasor rotation and its corresponding AC waveform generation
        def update_func(mob, dt):
            mob.rotate(0.1*TAU*dt)
            new_end = mob.get_end()
            projection_line.become(DashedLine(plane.c2p(0,0), plane.c2p(0, new_end[1]), color=RED))

        phasor.add_updater(update_func)
        self.add(phasor, projection_line)
        self.wait(5)  # Duration of phasor rotation and waveform generation

        phasor.remove_updater(update_func)
        
        # Euler's Relation
        euler_explanation = MathTex("e^{j\\theta} = \\cos(\\theta) + j\\sin(\\theta)").to_edge(DOWN)
        self.play(Write(euler_explanation))
        self.wait(2)

        # FadeOut 
        self.play(FadeOut(plane), FadeOut(title), FadeOut(explanation1), FadeOut(explanation2), 
                  FadeOut(phasor), FadeOut(projection_line), FadeOut(ac_waveform), FadeOut(ac_waveform_label),
                  FadeOut(euler_explanation))


class ACPhasorExplanation1(Scene):

    def construct(self):
        # Create a complex plane
        plane = ComplexPlane().scale(1)
        self.play(Create(plane))

        # Draw a circle of radius 1 (unit circle)


        # Function to get moving point
        def moving_point(t):
            return np.exp(1j * TAU * t)

        dot = Dot(plane.number_to_point(moving_point(0)), color=YELLOW)
        line = Line(plane.c2p(0,0), dot.get_center(), color=YELLOW)
       # label = MathTex("e^{i\\theta}").next_to(dot, RIGHT, buff=0.2)
        
        self.add(dot, line)

        def update_dot(mob, alpha):
            theta = interpolate(0, TAU, alpha)
            z_value = moving_point(theta)
            point = plane.number_to_point(z_value)
            mob.move_to(point)
            line.become(Line(plane.c2p(0,0), point, color=YELLOW))
            

        self.play(UpdateFromAlphaFunc(dot, update_dot), run_time=5)




class RotatingDot(Scene):
    def construct(self):
        # Create a complex plane
        plane = ComplexPlane().scale(1)
        self.play(Create(plane))

        title = Text("AC Phasor Representation", font_size=25, color=YELLOW).to_edge(UP)
        explanation1 = Text("In AC circuits, voltage or current can be represented as a rotating vector (phasor).", font_size=24, color=YELLOW).next_to(title, DOWN)
        explanation2 = Text("This phasor's projection on the vertical axis gives the instantaneous value of the AC signal.", font_size=24, color=YELLOW).next_to(explanation1, DOWN)
        self.play(Write(title), Write(explanation1), Write(explanation2))
        self.wait(2)

        # Function to get moving point
        def moving_point(t):
            return np.exp(1j * TAU * t)

        arrow = Arrow(plane.c2p(0, 0), plane.number_to_point(moving_point(0)), color=YELLOW, buff=0)
        self.add(arrow)
        points = VGroup()

        def update_arrow(mob, alpha):
            theta = interpolate(0, TAU, alpha)
            z_value = moving_point(theta)
            point = plane.number_to_point(z_value)
            mob.become(Arrow(plane.c2p(0, 0), point, color=YELLOW, buff=0))

           # Record the arrow tip for the dotted line
            dot = Dot(point, color=WHITE, radius=0.02).set_stroke(width=0.5)
            points.add(dot)
            
            wave = DashedLine(plane.c2p(0,0), point, dash_length=0.05).set_stroke(width=2)
            for p in points:
                wave.add_points_as_corners([p.get_center()])
            self.add(wave, dot)

        self.play(UpdateFromAlphaFunc(arrow, update_arrow), run_time=10)

        
        ac_waveform = ParametricFunction(
            lambda t: plane.c2p(t-3, np.sin(t*TAU)),
            t_range=[0, 2*PI],
            color=RED
        ).to_edge(RIGHT)
        ac_waveform_label = Text("AC Waveform", font_size=24).next_to(ac_waveform, UP)
        self.play(Create(ac_waveform), Write(ac_waveform_label))
        

        self.play(UpdateFromAlphaFunc(arrow, update_arrow), run_time=12)  # Increase run_time for slower rotation
        self.wait(2)














# from manim import *

# class ChangeInRealWorld(Scene):
#     def construct(self):
#         # Create a number line for time
#         time_line = NumberLine(
#             x_range=[0, 5, 1],
#             include_numbers=True,
#             include_tip=True,
#         )
#         time_line.set_width(8)
#         time_line.move_to(ORIGIN)

#         # Create a car and scale it down
#         car = ImageMobject("/Users/nathanfoale/Desktop/car.webp")
#         car.scale(0.2)
#         car.next_to(time_line.n2p(0), UP)  # Place car above number line

#         # Create labels for the car and speed graph
#         car_label = Text("Car's Speed", color=BLUE).next_to(car, UP)
#         time_label = Text("Time").next_to(time_line.get_right(), RIGHT)

#         # Create a function to represent the car's speed over time
#         def car_speed_function(x):
#             return 2 * x

#         # Create a graph for the car's speed without y-axis
#         car_speed_graph = Axes(
#             x_range=[0, 4, 1],
#             y_range=[0, 8, 1],
#             y_axis_config={"visible": False},  # Hide the y-axis
#             axis_config={"color": BLUE},
#         )
#         car_speed_graph.next_to(time_line, DOWN, buff=0.1)
#         car_speed_graph.plot(lambda x: car_speed_function(x), color=BLUE)

#         # Show stock price fluctuation
#         def stock_price_function(x):
#             return 2 * np.sin(x)

#         # Create stock price graph without y-axis
#         stock_price_graph = Axes(
#             x_range=[0, 4, 1],
#             y_range=[-2, 2, 1],
#             y_axis_config={"visible": False},  # Hide the y-axis
#             axis_config={"color": GREEN},
#         )
#         stock_price_graph.next_to(time_line, DOWN, buff=0.1)
#         stock_price_graph.plot(lambda x: stock_price_function(x), color=GREEN)
        
#         # Labels for stock price graph
#         stock_price_label = Text("Stock Price", color=GREEN).next_to(car_speed_graph, UP)

#         # Add to the scene
#         self.play(Create(time_line), Create(time_label))
#         self.play(FadeIn(car), Write(car_label))
#         self.play(FadeIn(car_speed_graph))
#         self.wait(2)

#         # Create car's trajectory over the timeline
#         car_trajectory = VMobject()
#         car_trajectory.set_points_smoothly([time_line.n2p(t) + UP * car.height / 2 for t in range(5)])
        
#         # Animate the car's movement smoothly
#         self.play(MoveAlongPath(car, car_trajectory), run_time=5)
#         self.wait(1)

#         # Transform the car speed graph to stock price graph
#         self.play(Transform(car_speed_graph, stock_price_graph), Transform(car_label, stock_price_label))
#         self.wait(2)

class EulersDerivative(Scene):
    def construct(self):
        # Create the separate parts of the formula
        part_e = MathTex(r"e^{i \theta}").scale(0.8)
        
        part_rest_of_formula = MathTex(r"   = \cos(\theta) + i \sin(\theta)").scale(0.8)
        formula_z = MathTex(r"z").scale(0.8)  
        derivative_formula = MathTex(r"\frac{dz}{d\theta} = -\sin(\theta) + i \cos(\theta)").scale(0.8)
        derivative_formula2 = MathTex(r" = i \cos(\theta) + i^2 \sin(\theta)").scale(0.8)
        derivative_formula3 = MathTex(r" = i(\cos(\theta) + i \sin(\theta))").scale(0.8)
        derivative_formula4 = MathTex(r"\frac{dz}{d\theta} = iz").scale(0.8)
        
        implication_result = MathTex(r"\frac{dz}{z} = i d\theta").scale(0.8)
        integrated_result = MathTex(r"\int \frac{dz}{z} = \int i d\theta").scale(0.8)
        integrated_result2 = MathTex(r"\ln(z) = i \theta + C").scale(0.8)
        integrated_result3 = MathTex(r"e^{\ln(z)} = e^{i \theta + c}").scale(0.8)
        integrated_result4 = MathTex(r"z = e^{i \theta}").scale(0.8)
        implies_symbol = MathTex(r"\Rightarrow").scale(1.2)
         
        
        


        
        part_e.next_to(part_rest_of_formula, LEFT)
        formula_e_to_z = VGroup(part_e, part_rest_of_formula).to_edge(UP)  
        formula_z.next_to(part_rest_of_formula, LEFT)

        

        # derivative formula
  

        
        derivative_formula.next_to(formula_e_to_z, DOWN)
        derivative_formula2.next_to(derivative_formula, DOWN).shift(RIGHT*0.3)
        derivative_formula3.next_to(derivative_formula2, DOWN)
        derivative_formula4.next_to(derivative_formula3, DOWN * 1).shift(LEFT * 2)
        implies_symbol.next_to(derivative_formula4, RIGHT, buff=0.5)
        implication_result.next_to(implies_symbol, RIGHT, buff=0.5)
        integrated_result.next_to(implies_symbol, DOWN * 1.2)
        integrated_result2.next_to(integrated_result, DOWN)
        integrated_result3.next_to(integrated_result2, DOWN)
        integrated_result4.next_to(integrated_result3, DOWN)
       

        #  circle representation
        circle = Circle(color=WHITE)
        circle_label = Tex("Unit Circle").scale(0.6).next_to(circle, UP, buff=0.1)

        
        circle_group = VGroup(circle, circle_label)

       
        circle_group.to_edge(RIGHT)

        # Creating the theta angle representation
        theta = MathTex(r"\theta").scale(0.6)
        theta.next_to(circle, DOWN, buff=0.4)

        # Drawing the radius for the complex number point
        radius = Line(circle.get_center(), circle.get_top(), color=YELLOW)
        
        # Creating the complex point on the circle
        dot = Dot(radius.get_end(), color=RED)

        # Grouping the radius and dot to rotate them later
        rotating_group = VGroup(radius, dot)

        # Adding everything to the scene
        self.play(FadeIn(formula_e_to_z), FadeIn(circle_group), FadeIn(theta))
        self.wait(1)
        self.play(Create(radius), Create(dot))
        self.wait(1)

        # Rotating the radius and dot to indicate theta changing
        self.play(rotating_group.animate.rotate(-PI/3, about_point=circle.get_center()))
        

        # Transform 'e^(i*theta)' into 'z'
        self.play(Transform(formula_e_to_z[0], formula_z))  # This transforms the e^(i*theta) part into z
        self.wait(1)

        # Show the derivative formula after the transformation
        self.play(Write(derivative_formula))
        self.wait(1)
        self.play(Write(derivative_formula2))
        self.wait(1)
        self.play(Write(derivative_formula3))
        self.wait(1)
        self.play(Write(derivative_formula4))
        self.wait(1)
        self.play(Write(implies_symbol))
        self.play(Write(implication_result))
        self.wait(1.5)
        self.play(Write(integrated_result))
        self.wait(1.5)
        self.play(Write(integrated_result2))
        self.wait(1.5)
        self.play(Write(integrated_result3))
        self.wait(1.5)
        self.play(Write(integrated_result4))

        

        # End of the scene
        self.wait(2)
