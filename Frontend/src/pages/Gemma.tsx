import { Card, CardContent } from '@/components/ui/card';
import { ArrowRight, MessageSquare, Video, FileText } from 'lucide-react';

const Gemma = () => {
  return (
    <div className="min-h-screen py-20 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-6 text-gradient fade-in-up">
            Beyond Detection: The Gemma Intelligence Layer
          </h1>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto fade-in-up stagger-1">
            Powered by Google's advanced AI, we transform thermal diagnosis into 
            comprehensive clinical support and multilingual patient communication.
          </p>
        </div>

        {/* Interactive Flowchart */}
        <section className="mb-20">
          <div className="relative">
            {/* Central Diagnosis */}
            <div className="flex justify-center mb-12 fade-in-up">
              <Card className="border-2 border-primary shadow-lg">
                <CardContent className="p-8 text-center">
                  <div className="w-16 h-16 gradient-clinical rounded-full flex items-center justify-center mx-auto mb-4">
                    <span className="text-white font-bold text-lg">AI</span>
                  </div>
                  <h3 className="text-xl font-bold text-primary">Diagnosis: Hypothermia</h3>
                  <p className="text-muted-foreground mt-2">Detected with 95% confidence</p>
                </CardContent>
              </Card>
            </div>

            {/* Arrow Down */}
            <div className="flex justify-center mb-8 fade-in-up stagger-1">
              <ArrowRight className="h-8 w-8 text-accent rotate-90" />
            </div>

            {/* Google AI Studio */}
            <div className="flex justify-center mb-12 fade-in-up stagger-2">
              <Card className="border-2 border-accent shadow-lg">
                <CardContent className="p-8 text-center">
                  <div className="w-20 h-20 bg-accent rounded-full flex items-center justify-center mx-auto mb-4">
                    <span className="text-white font-bold text-xl">G</span>
                  </div>
                  <h3 className="text-xl font-bold text-accent">Google AI Studio</h3>
                  <p className="text-muted-foreground mt-2">Gemma Large Language Model</p>
                </CardContent>
              </Card>
            </div>

            {/* Output Branches */}
            <div className="grid md:grid-cols-3 gap-8">
              <Card className="fade-in-left border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
                <CardContent className="p-8 text-center">
                  <div className="w-16 h-16 bg-blue-500 rounded-full flex items-center justify-center mx-auto mb-6">
                    <FileText className="h-8 w-8 text-white" />
                  </div>
                  <h3 className="text-xl font-bold mb-4">Clinical Plan</h3>
                  <p className="text-muted-foreground">
                    Detailed treatment protocol with step-by-step medical instructions for immediate care.
                  </p>
                </CardContent>
              </Card>

              <Card className="fade-in-up stagger-1 border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
                <CardContent className="p-8 text-center">
                  <div className="w-16 h-16 bg-green-500 rounded-full flex items-center justify-center mx-auto mb-6">
                    <MessageSquare className="h-8 w-8 text-white" />
                  </div>
                  <h3 className="text-xl font-bold mb-4">Parent Message</h3>
                  <p className="text-muted-foreground">
                    Multi-lingual, compassionate communication explaining the situation and next steps.
                  </p>
                </CardContent>
              </Card>

              <Card className="fade-in-right border-none shadow-lg hover:shadow-xl transition-shadow duration-300">
                <CardContent className="p-8 text-center">
                  <div className="w-16 h-16 bg-purple-500 rounded-full flex items-center justify-center mx-auto mb-6">
                    <Video className="h-8 w-8 text-white" />
                  </div>
                  <h3 className="text-xl font-bold mb-4">Instructional Video</h3>
                  <p className="text-muted-foreground">
                    Visual guides for proper care techniques and monitoring procedures.
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* AI Capabilities */}
        <section className="mb-20">
          <h2 className="text-3xl font-bold text-center mb-12 text-primary fade-in-up">
            AI-Powered Clinical Intelligence
          </h2>
          <div className="grid md:grid-cols-2 gap-8">
            <Card className="fade-in-left border-none shadow-lg">
              <CardContent className="p-8">
                <h3 className="text-xl font-bold mb-4 text-primary">Smart Clinical Protocols</h3>
                <ul className="space-y-3 text-muted-foreground">
                  <li className="flex items-start space-x-3">
                    <div className="w-2 h-2 bg-accent rounded-full mt-2"></div>
                    <span>Evidence-based treatment recommendations</span>
                  </li>
                  <li className="flex items-start space-x-3">
                    <div className="w-2 h-2 bg-accent rounded-full mt-2"></div>
                    <span>Dosage calculations and medication protocols</span>
                  </li>
                  <li className="flex items-start space-x-3">
                    <div className="w-2 h-2 bg-accent rounded-full mt-2"></div>
                    <span>Risk assessment and monitoring guidelines</span>
                  </li>
                  <li className="flex items-start space-x-3">
                    <div className="w-2 h-2 bg-accent rounded-full mt-2"></div>
                    <span>Follow-up care instructions</span>
                  </li>
                </ul>
              </CardContent>
            </Card>

            <Card className="fade-in-right border-none shadow-lg">
              <CardContent className="p-8">
                <h3 className="text-xl font-bold mb-4 text-primary">Multilingual Communication</h3>
                <ul className="space-y-3 text-muted-foreground">
                  <li className="flex items-start space-x-3">
                    <div className="w-2 h-2 bg-accent rounded-full mt-2"></div>
                    <span>Real-time translation in 50+ languages</span>
                  </li>
                  <li className="flex items-start space-x-3">
                    <div className="w-2 h-2 bg-accent rounded-full mt-2"></div>
                    <span>Culturally appropriate messaging</span>
                  </li>
                  <li className="flex items-start space-x-3">
                    <div className="w-2 h-2 bg-accent rounded-full mt-2"></div>
                    <span>Clear, jargon-free explanations</span>
                  </li>
                  <li className="flex items-start space-x-3">
                    <div className="w-2 h-2 bg-accent rounded-full mt-2"></div>
                    <span>Emotional support and reassurance</span>
                  </li>
                </ul>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Integration Benefits */}
        <section>
          <div className="text-center">
            <h2 className="text-3xl font-bold mb-8 text-primary fade-in-up">
              Why Gemma Integration Matters
            </h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
              <div className="fade-in-up">
                <div className="text-3xl font-bold text-accent mb-2">50+</div>
                <div className="text-muted-foreground">Languages Supported</div>
              </div>
              <div className="fade-in-up stagger-1">
                <div className="text-3xl font-bold text-accent mb-2">&lt;5s</div>
                <div className="text-muted-foreground">Response Generation</div>
              </div>
              <div className="fade-in-up stagger-2">
                <div className="text-3xl font-bold text-accent mb-2">24/7</div>
                <div className="text-muted-foreground">AI Availability</div>
              </div>
              <div className="fade-in-up stagger-3">
                <div className="text-3xl font-bold text-accent mb-2">99%</div>
                <div className="text-muted-foreground">Parent Satisfaction</div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Gemma;