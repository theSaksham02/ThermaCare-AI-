import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Heart, Users, Award, Target } from 'lucide-react';

const About = () => {
  return (
    <div className="min-h-screen py-20 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-6 text-gradient fade-in-up">
            About ThermoVision AI
          </h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto fade-in-up stagger-1">
            We're a dedicated team of engineers and medical professionals united by a single mission: 
            reducing neonatal mortality through accessible, intelligent technology.
          </p>
        </div>

        {/* Mission Statement */}
        <section className="mb-20">
          <Card className="border-none shadow-lg gradient-clinical text-white fade-in-up">
            <CardContent className="p-12 text-center">
              <Heart className="h-16 w-16 mx-auto mb-6 opacity-90" />
              <h2 className="text-3xl font-bold mb-6">Our Mission</h2>
              <p className="text-xl leading-relaxed max-w-4xl mx-auto opacity-95">
                Every year, over 2.4 million newborns die worldwide, many from preventable causes like 
                hypothermia. We believe that advanced technology should be accessible to every hospital, 
                clinic, and healthcare provider, regardless of location or resources. ThermoVision AI 
                transforms expensive, complex thermal monitoring into a simple, affordable solution 
                that saves lives.
              </p>
            </CardContent>
          </Card>
        </section>

        {/* Team Section */}
        <section className="mb-20">
          <h2 className="text-3xl font-bold text-center mb-12 text-gradient fade-in-up">
            Meet Our Team
          </h2>
          
          {/* Technical Team */}
          <div className="mb-16">
            <h3 className="text-2xl font-bold text-center mb-8 text-primary">Technical Team</h3>
            <div className="grid md:grid-cols-2 gap-8">
              {/* Saksham Mishra - Project Lead */}
              <Card className="fade-in-left border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
                <CardContent className="p-8 text-center">
                  <div className="w-32 h-32 gradient-clinical rounded-full mx-auto mb-6 flex items-center justify-center">
                    <span className="text-white text-4xl font-bold">SM</span>
                  </div>
                  <h3 className="text-2xl font-bold mb-2 text-primary">Saksham Mishra</h3>
                  <p className="text-muted-foreground mb-4">Project Lead</p>
                  <div className="flex flex-wrap gap-2 justify-center mb-6">
                    <Badge variant="secondary">Machine Learning</Badge>
                    <Badge variant="secondary">Project Management</Badge>
                    <Badge variant="secondary">AI Systems</Badge>
                  </div>
                  <p className="text-muted-foreground">
                    Leading the development of ThermoVision AI with expertise in machine learning 
                    and thermal imaging technologies. Passionate about creating accessible healthcare solutions.
                  </p>
                </CardContent>
              </Card>

              {/* Ankan Ganguli - Mentor */}
              <Card className="fade-in-right border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
                <CardContent className="p-8 text-center">
                  <div className="w-32 h-32 gradient-secondary rounded-full mx-auto mb-6 flex items-center justify-center">
                    <span className="text-white text-4xl font-bold">AG</span>
                  </div>
                  <h3 className="text-2xl font-bold mb-2 text-primary">Ankan Ganguli</h3>
                  <p className="text-muted-foreground mb-4">Mentor & Prompt Engineer</p>
                  <div className="flex flex-wrap gap-2 justify-center mb-6">
                    <Badge variant="secondary">AI Engineering</Badge>
                    <Badge variant="secondary">Prompt Design</Badge>
                    <Badge variant="secondary">Technical Mentorship</Badge>
                  </div>
                  <p className="text-muted-foreground">
                    Providing strategic guidance and expertise in AI prompt engineering. 
                    Specializes in optimizing language models for healthcare applications.
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>

          {/* Medical Team */}
          <div>
            <h3 className="text-2xl font-bold text-center mb-8 text-primary">Medical Team</h3>
            <div className="flex justify-center">
              <Card className="fade-in-up border-none shadow-lg hover:shadow-xl transition-shadow duration-300 max-w-md">
                <CardContent className="p-8 text-center">
                  <div className="w-32 h-32 bg-gradient-to-br from-pink-400 to-purple-500 rounded-full mx-auto mb-6 flex items-center justify-center">
                    <span className="text-white text-4xl font-bold">AS</span>
                  </div>
                  <h3 className="text-2xl font-bold mb-2 text-primary">Ashi Soni</h3>
                  <p className="text-muted-foreground mb-4">Medical Advisor</p>
                  <div className="flex flex-wrap gap-2 justify-center mb-6">
                    <Badge variant="secondary">Clinical Expertise</Badge>
                    <Badge variant="secondary">Medical Validation</Badge>
                    <Badge variant="secondary">Healthcare Innovation</Badge>
                  </div>
                  <p className="text-muted-foreground">
                    Ensures clinical accuracy and validates our thermal monitoring solutions. 
                    Bridges the gap between technology and real-world medical applications.
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Company Values */}
        <section className="mb-20">
          <h2 className="text-3xl font-bold text-center mb-12 text-primary fade-in-up">
            Our Values
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <Card className="fade-in-up border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Heart className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-bold mb-2">Life First</h3>
                <p className="text-sm text-muted-foreground">
                  Every decision prioritizes patient outcomes and safety
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-1 border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Users className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-bold mb-2">Universal Access</h3>
                <p className="text-sm text-muted-foreground">
                  Advanced healthcare technology should be accessible everywhere
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-2 border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Award className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-bold mb-2">Clinical Excellence</h3>
                <p className="text-sm text-muted-foreground">
                  Rigorous validation and continuous improvement
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-3 border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Target className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-bold mb-2">Simplicity</h3>
                <p className="text-sm text-muted-foreground">
                  Complex technology made simple and intuitive
                </p>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Impact Statistics */}
        <section className="mb-20">
          <h2 className="text-3xl font-bold text-center mb-12 text-primary fade-in-up">
            Our Impact
          </h2>
          <div className="grid md:grid-cols-4 gap-8 text-center">
            <div className="fade-in-up">
              <div className="text-4xl font-bold text-accent mb-2">2.4M</div>
              <div className="text-muted-foreground">Newborns at risk annually</div>
            </div>
            <div className="fade-in-up stagger-1">
              <div className="text-4xl font-bold text-accent mb-2">95%</div>
              <div className="text-muted-foreground">Detection accuracy achieved</div>
            </div>
            <div className="fade-in-up stagger-2">
              <div className="text-4xl font-bold text-accent mb-2">50+</div>
              <div className="text-muted-foreground">Languages supported</div>
            </div>
            <div className="fade-in-up stagger-3">
              <div className="text-4xl font-bold text-accent mb-2">24/7</div>
              <div className="text-muted-foreground">Continuous monitoring</div>
            </div>
          </div>
        </section>

        {/* Recognition */}
        <section>
          <h2 className="text-3xl font-bold text-center mb-12 text-primary fade-in-up">
            Recognition & Partnerships
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <Card className="fade-in-left border-none shadow-lg text-center">
              <CardContent className="p-8">
                <div className="w-16 h-16 bg-blue-500 rounded-full mx-auto mb-4 flex items-center justify-center">
                  <Award className="h-8 w-8 text-white" />
                </div>
                <h3 className="font-bold mb-2">Medical Innovation Award</h3>
                <p className="text-sm text-muted-foreground">
                  Recognized for breakthrough in neonatal care technology
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-1 border-none shadow-lg text-center">
              <CardContent className="p-8">
                <div className="w-16 h-16 bg-green-500 rounded-full mx-auto mb-4 flex items-center justify-center">
                  <Users className="h-8 w-8 text-white" />
                </div>
                <h3 className="font-bold mb-2">Google AI Partnership</h3>
                <p className="text-sm text-muted-foreground">
                  Collaborating with Google's Gemma for advanced AI capabilities
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-right border-none shadow-lg text-center">
              <CardContent className="p-8">
                <div className="w-16 h-16 bg-purple-500 rounded-full mx-auto mb-4 flex items-center justify-center">
                  <Heart className="h-8 w-8 text-white" />
                </div>
                <h3 className="font-bold mb-2">Healthcare Excellence</h3>
                <p className="text-sm text-muted-foreground">
                  Endorsed by leading neonatal care specialists worldwide
                </p>
              </CardContent>
            </Card>
          </div>
        </section>
      </div>
    </div>
  );
};

export default About;