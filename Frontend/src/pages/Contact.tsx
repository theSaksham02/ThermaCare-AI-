import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Label } from '@/components/ui/label';
import { Mail, Phone, MapPin, Clock } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    organization: '',
    message: ''
  });
  const { toast } = useToast();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission here
    toast({
      title: "Message sent successfully!",
      description: "We'll get back to you within 24 hours.",
    });
    setFormData({ name: '', email: '', organization: '', message: '' });
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  return (
    <div className="min-h-screen py-20 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-6 text-gradient fade-in-up">
            Get In Touch
          </h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto fade-in-up stagger-1">
            Ready to transform neonatal care at your facility? We'd love to hear from you. 
            Reach out to discuss how ThermoVision AI can make a difference in your NICU.
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-12">
          {/* Contact Form */}
          <Card className="fade-in-left border-none shadow-lg">
            <CardHeader>
              <CardTitle className="text-2xl text-primary">Send Us a Message</CardTitle>
            </CardHeader>
            <CardContent>
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="space-y-2">
                  <Label htmlFor="name">Full Name *</Label>
                  <Input
                    id="name"
                    name="name"
                    type="text"
                    required
                    value={formData.name}
                    onChange={handleChange}
                    placeholder="Dr. Jane Smith"
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="email">Email Address *</Label>
                  <Input
                    id="email"
                    name="email"
                    type="email"
                    required
                    value={formData.email}
                    onChange={handleChange}
                    placeholder="jane.smith@hospital.com"
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="organization">Hospital/Organization</Label>
                  <Input
                    id="organization"
                    name="organization"
                    type="text"
                    value={formData.organization}
                    onChange={handleChange}
                    placeholder="Children's Hospital"
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="message">Message *</Label>
                  <Textarea
                    id="message"
                    name="message"
                    required
                    value={formData.message}
                    onChange={handleChange}
                    placeholder="Tell us about your NICU and how we can help..."
                    rows={5}
                  />
                </div>

                <Button 
                  type="submit" 
                  className="w-full bg-accent hover:bg-accent/90"
                  size="lg"
                >
                  Send Message
                </Button>
              </form>
            </CardContent>
          </Card>

          {/* Contact Information */}
          <div className="space-y-8 fade-in-right">
            {/* Contact Details */}
            <Card className="border-none shadow-lg">
              <CardHeader>
                <CardTitle className="text-2xl text-primary">Contact Information</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="flex items-start space-x-4">
                  <Mail className="h-6 w-6 text-accent mt-1" />
                  <div>
                    <h3 className="font-semibold mb-1">Email</h3>
                    <p className="text-muted-foreground">info@thermovision-ai.com</p>
                    <p className="text-muted-foreground">support@thermovision-ai.com</p>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <Phone className="h-6 w-6 text-accent mt-1" />
                  <div>
                    <h3 className="font-semibold mb-1">Phone</h3>
                    <p className="text-muted-foreground">+1 (555) 123-4567</p>
                    <p className="text-sm text-muted-foreground">24/7 Emergency Support</p>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <MapPin className="h-6 w-6 text-accent mt-1" />
                  <div>
                    <h3 className="font-semibold mb-1">Address</h3>
                    <p className="text-muted-foreground">
                      123 Medical Innovation Drive<br />
                      Healthcare District<br />
                      San Francisco, CA 94105
                    </p>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <Clock className="h-6 w-6 text-accent mt-1" />
                  <div>
                    <h3 className="font-semibold mb-1">Business Hours</h3>
                    <p className="text-muted-foreground">
                      Monday - Friday: 8:00 AM - 6:00 PM PST<br />
                      Emergency Support: 24/7
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Quick Links */}
            <Card className="border-none shadow-lg">
              <CardHeader>
                <CardTitle className="text-xl text-primary">Need Immediate Help?</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="space-y-3">
                  <Button variant="outline" className="w-full justify-start" asChild>
                    <a href="/demo">
                      <span>Request a Demo</span>
                    </a>
                  </Button>
                  <Button variant="outline" className="w-full justify-start" asChild>
                    <a href="/technology">
                      <span>View Technical Specifications</span>
                    </a>
                  </Button>
                  <Button variant="outline" className="w-full justify-start" asChild>
                    <a href="mailto:support@thermovision-ai.com">
                      <span>Technical Support</span>
                    </a>
                  </Button>
                </div>
              </CardContent>
            </Card>

            {/* Response Time */}
            <Card className="border-none shadow-lg gradient-clinical text-white">
              <CardContent className="p-6 text-center">
                <Clock className="h-12 w-12 mx-auto mb-4 opacity-90" />
                <h3 className="text-xl font-bold mb-2">Fast Response Time</h3>
                <p className="opacity-95">
                  We typically respond to all inquiries within 4 hours during business hours, 
                  and provide 24/7 emergency support for existing customers.
                </p>
              </CardContent>
            </Card>
          </div>
        </div>

        {/* FAQ Section */}
        <section className="mt-20">
          <h2 className="text-3xl font-bold text-center mb-12 text-primary fade-in-up">
            Frequently Asked Questions
          </h2>
          <div className="grid md:grid-cols-2 gap-8">
            <Card className="fade-in-left border-none shadow-lg">
              <CardContent className="p-6">
                <h3 className="font-bold mb-3 text-primary">How quickly can we get started?</h3>
                <p className="text-muted-foreground">
                  Most pilot programs can be set up within 2-3 weeks, including training and installation. 
                  Full department rollouts typically take 4-6 weeks.
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-right border-none shadow-lg">
              <CardContent className="p-6">
                <h3 className="font-bold mb-3 text-primary">What kind of training is provided?</h3>
                <p className="text-muted-foreground">
                  We provide comprehensive on-site training for all medical staff, plus ongoing 
                  virtual support and regular check-ins to ensure optimal usage.
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-left border-none shadow-lg">
              <CardContent className="p-6">
                <h3 className="font-bold mb-3 text-primary">Is the system HIPAA compliant?</h3>
                <p className="text-muted-foreground">
                  Yes, ThermoVision AI is fully HIPAA compliant with end-to-end encryption, 
                  secure data storage, and comprehensive audit trails.
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-right border-none shadow-lg">
              <CardContent className="p-6">
                <h3 className="font-bold mb-3 text-primary">What ongoing support is available?</h3>
                <p className="text-muted-foreground">
                  24/7 technical support, regular software updates, maintenance, and clinical 
                  consultation services are all included in our support packages.
                </p>
              </CardContent>
            </Card>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Contact;