import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Smartphone, Monitor, Wifi, Battery } from 'lucide-react';

const Product = () => {
  return (
    <div className="min-h-screen py-20 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-6 text-gradient fade-in-up">
            Simple, Powerful, Accessible
          </h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto fade-in-up stagger-1">
            Our complete thermal monitoring solution combines cutting-edge hardware 
            with intuitive software for seamless integration into any clinical environment.
          </p>
        </div>

        {/* Product Gallery */}
        <section className="mb-20">
          <div className="grid lg:grid-cols-3 gap-8">
            {/* FLIR Camera */}
            <Card className="fade-in-left border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardHeader>
                <CardTitle className="text-center">FLIR Thermal Camera</CardTitle>
              </CardHeader>
              <CardContent className="p-6">
                <div className="aspect-square bg-gradient-to-br from-gray-100 to-gray-200 rounded-lg flex items-center justify-center mb-4">
                  <div className="w-32 h-20 bg-gray-800 rounded-lg flex items-center justify-center">
                    <div className="w-16 h-12 bg-red-500 rounded opacity-70"></div>
                  </div>
                </div>
                <p className="text-muted-foreground text-center">
                  Professional-grade thermal imaging with smartphone integration
                </p>
                <div className="mt-4 flex flex-wrap gap-2 justify-center">
                  <Badge variant="secondary">High Resolution</Badge>
                  <Badge variant="secondary">USB-C</Badge>
                  <Badge variant="secondary">Portable</Badge>
                </div>
              </CardContent>
            </Card>

            {/* Mobile App */}
            <Card className="fade-in-up stagger-1 border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardHeader>
                <CardTitle className="text-center">Mobile Application</CardTitle>
              </CardHeader>
              <CardContent className="p-6">
                <div className="aspect-square bg-gradient-to-br from-blue-100 to-blue-200 rounded-lg flex items-center justify-center mb-4">
                  <Smartphone className="h-24 w-24 text-primary" />
                </div>
                <p className="text-muted-foreground text-center">
                  Intuitive interface for real-time thermal analysis and diagnosis
                </p>
                <div className="mt-4 flex flex-wrap gap-2 justify-center">
                  <Badge variant="secondary">iOS</Badge>
                  <Badge variant="secondary">Android</Badge>
                  <Badge variant="secondary">Real-time</Badge>
                </div>
              </CardContent>
            </Card>

            {/* Nurse Dashboard */}
            <Card className="fade-in-right border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardHeader>
                <CardTitle className="text-center">Nurse Dashboard</CardTitle>
              </CardHeader>
              <CardContent className="p-6">
                <div className="aspect-square bg-gradient-to-br from-green-100 to-green-200 rounded-lg flex items-center justify-center mb-4">
                  <Monitor className="h-24 w-24 text-accent" />
                </div>
                <p className="text-muted-foreground text-center">
                  Comprehensive monitoring interface with patient management
                </p>
                <div className="mt-4 flex flex-wrap gap-2 justify-center">
                  <Badge variant="secondary">Web-based</Badge>
                  <Badge variant="secondary">Multi-patient</Badge>
                  <Badge variant="secondary">Alerts</Badge>
                </div>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Technical Specifications */}
        <section className="mb-20">
          <h2 className="text-3xl font-bold text-center mb-12 text-primary fade-in-up">
            Technical Specifications
          </h2>
          <div className="grid md:grid-cols-2 gap-8">
            <Card className="fade-in-left border-none shadow-lg">
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <Smartphone className="h-6 w-6 text-primary" />
                  <span>Hardware Requirements</span>
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Camera Resolution</span>
                  <span className="font-semibold">320 × 240 pixels</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Temperature Range</span>
                  <span className="font-semibold">-10°C to +400°C</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Accuracy</span>
                  <span className="font-semibold">±0.3°C</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Frame Rate</span>
                  <span className="font-semibold">30 Hz</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Connectivity</span>
                  <span className="font-semibold">USB-C, Bluetooth</span>
                </div>
              </CardContent>
            </Card>

            <Card className="fade-in-right border-none shadow-lg">
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <Monitor className="h-6 w-6 text-primary" />
                  <span>Software Features</span>
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex justify-between">
                  <span className="text-muted-foreground">AI Processing</span>
                  <span className="font-semibold">Real-time</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Cloud Integration</span>
                  <span className="font-semibold">HIPAA Compliant</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Languages</span>
                  <span className="font-semibold">50+</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Data Export</span>
                  <span className="font-semibold">PDF, CSV, HL7</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Updates</span>
                  <span className="font-semibold">Over-the-air</span>
                </div>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Key Features */}
        <section className="mb-20">
          <h2 className="text-3xl font-bold text-center mb-12 text-primary fade-in-up">
            Key Features
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <Card className="fade-in-up border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Wifi className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-semibold mb-2">Wireless Connectivity</h3>
                <p className="text-sm text-muted-foreground">
                  Seamless data transmission to hospital systems
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-1 border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Battery className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-semibold mb-2">Long Battery Life</h3>
                <p className="text-sm text-muted-foreground">
                  12+ hours of continuous operation
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-2 border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Monitor className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-semibold mb-2">Multi-Platform</h3>
                <p className="text-sm text-muted-foreground">
                  Works on tablets, phones, and computers
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-3 border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Smartphone className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-semibold mb-2">Easy Integration</h3>
                <p className="text-sm text-muted-foreground">
                  Quick setup with existing hospital infrastructure
                </p>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Deployment Options */}
        <section>
          <h2 className="text-3xl font-bold text-center mb-12 text-primary fade-in-up">
            Deployment Options
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <Card className="fade-in-left border-none shadow-lg">
              <CardHeader>
                <CardTitle className="text-center text-primary">Pilot Program</CardTitle>
              </CardHeader>
              <CardContent className="text-center p-6">
                <div className="text-3xl font-bold text-accent mb-4">1-5</div>
                <div className="text-sm text-muted-foreground mb-4">Units</div>
                <p className="text-muted-foreground">
                  Perfect for initial testing and validation in your NICU environment.
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-1 border-2 border-primary shadow-lg">
              <CardHeader>
                <CardTitle className="text-center text-primary">Department Rollout</CardTitle>
                <div className="text-center">
                  <Badge className="bg-accent">Most Popular</Badge>
                </div>
              </CardHeader>
              <CardContent className="text-center p-6">
                <div className="text-3xl font-bold text-accent mb-4">5-20</div>
                <div className="text-sm text-muted-foreground mb-4">Units</div>
                <p className="text-muted-foreground">
                  Full department coverage with comprehensive training and support.
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-right border-none shadow-lg">
              <CardHeader>
                <CardTitle className="text-center text-primary">Hospital-wide</CardTitle>
              </CardHeader>
              <CardContent className="text-center p-6">
                <div className="text-3xl font-bold text-accent mb-4">20+</div>
                <div className="text-sm text-muted-foreground mb-4">Units</div>
                <p className="text-muted-foreground">
                  Enterprise solution with custom integration and 24/7 support.
                </p>
              </CardContent>
            </Card>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Product;