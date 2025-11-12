import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Checkbox } from '@/components/ui/checkbox';
import { Calendar, Users, Clock, CheckCircle } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

const Demo = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    title: '',
    organization: '',
    phone: '',
    nicu_size: '',
    current_solution: '',
    timeline: '',
    specific_interests: '',
    preferred_time: '',
    additional_notes: ''
  });
  const [agreeToTerms, setAgreeToTerms] = useState(false);
  const { toast } = useToast();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!agreeToTerms) {
      toast({
        title: "Please agree to terms",
        description: "You must agree to the terms and conditions to proceed.",
        variant: "destructive"
      });
      return;
    }
    // Handle form submission here - this will eventually trigger app.py
    toast({
      title: "Demo request submitted!",
      description: "We'll contact you within 24 hours to schedule your personalized demo.",
    });
    setFormData({
      name: '', email: '', title: '', organization: '', phone: '', nicu_size: '',
      current_solution: '', timeline: '', specific_interests: '', preferred_time: '', additional_notes: ''
    });
    setAgreeToTerms(false);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  const handleSelectChange = (name: string, value: string) => {
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  return (
    <div className="min-h-screen py-20 px-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-6 text-gradient fade-in-up">
            Request Your Demo
          </h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto fade-in-up stagger-1">
            See ThermoVision AI in action. Schedule a personalized demonstration 
            tailored to your NICU's specific needs and requirements.
          </p>
        </div>

        {/* Demo Benefits */}
        <section className="mb-12">
          <div className="grid md:grid-cols-3 gap-6">
            <Card className="fade-in-up border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Calendar className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-bold mb-2">Live Demonstration</h3>
                <p className="text-sm text-muted-foreground">
                  See real thermal analysis in action with actual case studies
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-1 border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Users className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-bold mb-2">Personalized</h3>
                <p className="text-sm text-muted-foreground">
                  Customized presentation based on your facility's specific needs
                </p>
              </CardContent>
            </Card>

            <Card className="fade-in-up stagger-2 border-none shadow-lg text-center">
              <CardContent className="p-6">
                <Clock className="h-12 w-12 text-accent mx-auto mb-4" />
                <h3 className="font-bold mb-2">30-45 Minutes</h3>
                <p className="text-sm text-muted-foreground">
                  Comprehensive overview including Q&A session
                </p>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Demo Request Form */}
        <Card className="fade-in-up border-none shadow-lg">
          <CardHeader className="text-center">
            <CardTitle className="text-2xl text-primary">Schedule Your Demo</CardTitle>
            <p className="text-muted-foreground">
              Fill out the form below and we'll contact you within 24 hours to schedule your demo.
            </p>
          </CardHeader>
          <CardContent className="p-8">
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Basic Information */}
              <div className="grid md:grid-cols-2 gap-6">
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
              </div>

              <div className="grid md:grid-cols-2 gap-6">
                <div className="space-y-2">
                  <Label htmlFor="title">Job Title *</Label>
                  <Input
                    id="title"
                    name="title"
                    type="text"
                    required
                    value={formData.title}
                    onChange={handleChange}
                    placeholder="Chief of Neonatology"
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="phone">Phone Number</Label>
                  <Input
                    id="phone"
                    name="phone"
                    type="tel"
                    value={formData.phone}
                    onChange={handleChange}
                    placeholder="+1 (555) 123-4567"
                  />
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="organization">Hospital/Organization *</Label>
                <Input
                  id="organization"
                  name="organization"
                  type="text"
                  required
                  value={formData.organization}
                  onChange={handleChange}
                  placeholder="Children's Hospital of Philadelphia"
                />
              </div>

              {/* NICU Information */}
              <div className="grid md:grid-cols-2 gap-6">
                <div className="space-y-2">
                  <Label htmlFor="nicu_size">NICU Size</Label>
                  <Select onValueChange={(value) => handleSelectChange('nicu_size', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select NICU size" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="small">Small (1-20 beds)</SelectItem>
                      <SelectItem value="medium">Medium (21-50 beds)</SelectItem>
                      <SelectItem value="large">Large (51-100 beds)</SelectItem>
                      <SelectItem value="extra_large">Extra Large (100+ beds)</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-2">
                  <Label htmlFor="timeline">Implementation Timeline</Label>
                  <Select onValueChange={(value) => handleSelectChange('timeline', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select timeline" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="immediate">Immediate (within 1 month)</SelectItem>
                      <SelectItem value="short">Short-term (1-3 months)</SelectItem>
                      <SelectItem value="medium">Medium-term (3-6 months)</SelectItem>
                      <SelectItem value="long">Long-term (6+ months)</SelectItem>
                      <SelectItem value="planning">Planning phase</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="current_solution">Current Temperature Monitoring Solution</Label>
                <Input
                  id="current_solution"
                  name="current_solution"
                  type="text"
                  value={formData.current_solution}
                  onChange={handleChange}
                  placeholder="e.g., Traditional thermometers, existing thermal imaging system"
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="preferred_time">Preferred Demo Time</Label>
                <Select onValueChange={(value) => handleSelectChange('preferred_time', value)}>
                  <SelectTrigger>
                    <SelectValue placeholder="Select preferred time" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="morning">Morning (9 AM - 12 PM)</SelectItem>
                    <SelectItem value="afternoon">Afternoon (12 PM - 5 PM)</SelectItem>
                    <SelectItem value="evening">Evening (5 PM - 7 PM)</SelectItem>
                    <SelectItem value="flexible">Flexible</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <Label htmlFor="specific_interests">Specific Areas of Interest</Label>
                <Textarea
                  id="specific_interests"
                  name="specific_interests"
                  value={formData.specific_interests}
                  onChange={handleChange}
                  placeholder="e.g., Integration with existing systems, staff training, clinical workflow..."
                  rows={3}
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="additional_notes">Additional Notes</Label>
                <Textarea
                  id="additional_notes"
                  name="additional_notes"
                  value={formData.additional_notes}
                  onChange={handleChange}
                  placeholder="Any additional information or questions..."
                  rows={3}
                />
              </div>

              {/* Terms Agreement */}
              <div className="flex items-start space-x-3">
                <Checkbox
                  id="terms"
                  checked={agreeToTerms}
                  onCheckedChange={(checked) => setAgreeToTerms(checked === true)}
                />
                <Label htmlFor="terms" className="text-sm text-muted-foreground leading-relaxed">
                  I agree to receive communications from ThermoVision AI regarding this demo request and 
                  understand that my information will be handled according to the privacy policy. *
                </Label>
              </div>

              <Button 
                type="submit" 
                className="w-full bg-accent hover:bg-accent/90"
                size="lg"
                disabled={!agreeToTerms}
              >
                Request Demo
              </Button>
            </form>
          </CardContent>
        </Card>

        {/* What to Expect */}
        <section className="mt-16">
          <Card className="border-none shadow-lg gradient-clinical text-white">
            <CardContent className="p-8">
              <h2 className="text-2xl font-bold text-center mb-8">What to Expect</h2>
              <div className="grid md:grid-cols-2 gap-8">
                <div className="space-y-4">
                  <div className="flex items-start space-x-3">
                    <CheckCircle className="h-6 w-6 mt-1 opacity-90" />
                    <div>
                      <h3 className="font-semibold mb-1">Pre-Demo Consultation</h3>
                      <p className="text-sm opacity-90">
                        Brief call to understand your specific needs and customize the demonstration
                      </p>
                    </div>
                  </div>
                  <div className="flex items-start space-x-3">
                    <CheckCircle className="h-6 w-6 mt-1 opacity-90" />
                    <div>
                      <h3 className="font-semibold mb-1">Live Product Demo</h3>
                      <p className="text-sm opacity-90">
                        Complete walkthrough of the ThermoVision AI system with real case examples
                      </p>
                    </div>
                  </div>
                </div>
                <div className="space-y-4">
                  <div className="flex items-start space-x-3">
                    <CheckCircle className="h-6 w-6 mt-1 opacity-90" />
                    <div>
                      <h3 className="font-semibold mb-1">Q&A Session</h3>
                      <p className="text-sm opacity-90">
                        Detailed discussion about integration, training, and implementation
                      </p>
                    </div>
                  </div>
                  <div className="flex items-start space-x-3">
                    <CheckCircle className="h-6 w-6 mt-1 opacity-90" />
                    <div>
                      <h3 className="font-semibold mb-1">Next Steps</h3>
                      <p className="text-sm opacity-90">
                        Clear roadmap for pilot program or full implementation at your facility
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </section>
      </div>
    </div>
  );
};

export default Demo;