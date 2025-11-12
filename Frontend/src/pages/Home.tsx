import { Link } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { Eye, Brain, Activity } from 'lucide-react';

const Home = () => {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-screen flex items-center justify-center gradient-clinical">
        <div className="absolute inset-0 bg-black/20"></div>
        <div className="relative z-10 text-center text-white px-4 max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-7xl font-bold mb-6 fade-in-up">
            Intelligent Thermal Monitoring for Every Newborn
          </h1>
          <p className="text-xl md:text-2xl mb-8 opacity-90 fade-in-up stagger-1">
            Turning heat data into life-saving clinical decisions
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center fade-in-up stagger-2">
            <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-lg px-8 py-3">
              <Link to="/demo">Request a Demo</Link>
            </Button>
            <Button asChild variant="outline" size="lg" className="text-lg px-8 py-3 border-white text-white hover:bg-white hover:text-primary">
              <Link to="/technology">Learn More</Link>
            </Button>
          </div>
        </div>
      </section>

      {/* What We Do Section */}
      <section className="py-20 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold text-center mb-16 text-gradient">
            What We Do
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <Card className="fade-in-up border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardContent className="p-8 text-center">
                <div className="w-16 h-16 gradient-clinical rounded-full flex items-center justify-center mx-auto mb-6">
                  <Eye className="h-8 w-8 text-white" />
                </div>
                <h3 className="text-2xl font-bold mb-4 text-primary">Detect</h3>
                <p className="text-muted-foreground">
                  Non-contact thermal screening to instantly detect signs of hypo/hyperthermia in newborns.
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-1 border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardContent className="p-8 text-center">
                <div className="w-16 h-16 gradient-clinical rounded-full flex items-center justify-center mx-auto mb-6">
                  <Brain className="h-8 w-8 text-white" />
                </div>
                <h3 className="text-2xl font-bold mb-4 text-primary">Analyze</h3>
                <p className="text-muted-foreground">
                  Our AI model analyzes thermal patterns with high accuracy to provide clear diagnosis.
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-2 border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardContent className="p-8 text-center">
                <div className="w-16 h-16 gradient-clinical rounded-full flex items-center justify-center mx-auto mb-6">
                  <Activity className="h-8 w-8 text-white" />
                </div>
                <h3 className="text-2xl font-bold mb-4 text-primary">Act</h3>
                <p className="text-muted-foreground">
                  Google's Gemma generates immediate, actionable clinical guidance for medical staff.
                </p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-20 bg-secondary">
        <div className="max-w-6xl mx-auto px-4">
          <div className="grid md:grid-cols-3 gap-8 text-center">
            <div className="fade-in-up">
              <div className="text-4xl font-bold text-primary mb-2">95%</div>
              <div className="text-muted-foreground">Detection Accuracy</div>
            </div>
            <div className="fade-in-up stagger-1">
              <div className="text-4xl font-bold text-primary mb-2">&lt;30s</div>
              <div className="text-muted-foreground">Analysis Time</div>
            </div>
            <div className="fade-in-up stagger-2">
              <div className="text-4xl font-bold text-primary mb-2">24/7</div>
              <div className="text-muted-foreground">Continuous Monitoring</div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold mb-6 fade-in-up">
            Ready to Transform Neonatal Care?
          </h2>
          <p className="text-xl text-muted-foreground mb-8 fade-in-up stagger-1">
            Join leading hospitals and clinics using ThermoVision AI to save more lives.
          </p>
          <Button asChild size="lg" className="bg-accent hover:bg-accent/90 text-lg px-8 py-3 fade-in-up stagger-2">
            <Link to="/demo">Get Started Today</Link>
          </Button>
        </div>
      </section>
    </div>
  );
};

export default Home;