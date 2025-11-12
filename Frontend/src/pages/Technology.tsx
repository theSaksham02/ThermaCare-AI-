import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Thermometer, Zap, Shield, Target } from 'lucide-react';

const Technology = () => {
  return (
    <div className="min-h-screen py-20 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-6 text-gradient fade-in-up">
            Our Technology
          </h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto fade-in-up stagger-1">
            Advanced thermal imaging combined with machine learning to deliver precise, 
            non-invasive temperature monitoring for neonatal care.
          </p>
        </div>

        {/* Thermal Analysis Section */}
        <section className="mb-20">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div className="fade-in-left">
              <h2 className="text-3xl font-bold mb-6 text-primary">
                High-Resolution Thermal Analysis
              </h2>
              <div className="space-y-4">
                <div className="flex items-center space-x-3">
                  <Thermometer className="h-6 w-6 text-accent" />
                  <span className="text-lg">Non-invasive thermal imaging</span>
                </div>
                <div className="flex items-center space-x-3">
                  <Zap className="h-6 w-6 text-accent" />
                  <span className="text-lg">HSV + LBP feature extraction</span>
                </div>
                <div className="flex items-center space-x-3">
                  <Shield className="h-6 w-6 text-accent" />
                  <span className="text-lg">Safe for continuous monitoring</span>
                </div>
                <div className="flex items-center space-x-3">
                  <Target className="h-6 w-6 text-accent" />
                  <span className="text-lg">Precise temperature detection</span>
                </div>
              </div>
            </div>
            <div className="fade-in-right">
              <Card className="border-none shadow-lg">
                <CardContent className="p-8">
                  <div className="aspect-video bg-gradient-to-br from-blue-500 to-red-500 rounded-lg flex items-center justify-center">
                    <div className="text-white text-center">
                      <Thermometer className="h-16 w-16 mx-auto mb-4" />
                      <p className="text-lg font-semibold">Thermal Image Analysis</p>
                      <p className="text-sm opacity-90">Real-time temperature mapping</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Model Performance Section */}
        <section className="mb-20">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold mb-4 text-primary fade-in-up">
              Clinically Validated Performance
            </h2>
            <p className="text-lg text-muted-foreground fade-in-up stagger-1">
              Our RandomForest model achieved exceptional results, including perfect detection 
              rate for hypothermia in our test dataset.
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {/* Confusion Matrix Placeholder */}
            <Card className="fade-in-left border-none shadow-lg">
              <CardHeader>
                <CardTitle className="text-center">Confusion Matrix</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="aspect-square bg-secondary rounded-lg flex items-center justify-center">
                  <div className="text-center">
                    <div className="text-3xl font-bold text-primary mb-2">100%</div>
                    <div className="text-sm text-muted-foreground">Hypothermia Detection</div>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Performance Metrics */}
            <Card className="fade-in-right border-none shadow-lg">
              <CardHeader>
                <CardTitle className="text-center">Model Metrics</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex justify-between items-center">
                  <span>Accuracy</span>
                  <Badge variant="secondary" className="bg-green-100 text-green-800">95.2%</Badge>
                </div>
                <div className="flex justify-between items-center">
                  <span>Precision</span>
                  <Badge variant="secondary" className="bg-blue-100 text-blue-800">94.8%</Badge>
                </div>
                <div className="flex justify-between items-center">
                  <span>Recall</span>
                  <Badge variant="secondary" className="bg-purple-100 text-purple-800">96.1%</Badge>
                </div>
                <div className="flex justify-between items-center">
                  <span>F1-Score</span>
                  <Badge variant="secondary" className="bg-orange-100 text-orange-800">95.4%</Badge>
                </div>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Technical Features */}
        <section>
          <h2 className="text-3xl font-bold text-center mb-12 text-primary fade-in-up">
            Technical Features
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            <Card className="fade-in-up border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardContent className="p-6">
                <h3 className="text-lg font-semibold mb-3 text-primary">Machine Learning</h3>
                <p className="text-muted-foreground">
                  RandomForest algorithm optimized for thermal pattern recognition with 95%+ accuracy.
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-1 border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardContent className="p-6">
                <h3 className="text-lg font-semibold mb-3 text-primary">Real-time Processing</h3>
                <p className="text-muted-foreground">
                  Instant analysis and diagnosis within 30 seconds of thermal image capture.
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-2 border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardContent className="p-6">
                <h3 className="text-lg font-semibold mb-3 text-primary">Continuous Monitoring</h3>
                <p className="text-muted-foreground">
                  24/7 automated monitoring with intelligent alerts for medical staff.
                </p>
              </CardContent>
            </Card>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Technology;