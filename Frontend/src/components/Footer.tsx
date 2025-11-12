import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="bg-secondary border-t border-border py-12">
      <div className="max-w-6xl mx-auto px-4">
        <div className="grid md:grid-cols-4 gap-8">
          <div>
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-8 h-8 gradient-clinical rounded-lg flex items-center justify-center">
                <span className="text-primary-foreground font-bold text-sm">TV</span>
              </div>
              <span className="text-xl font-bold text-gradient">ThermoVision AI</span>
            </div>
            <p className="text-muted-foreground text-sm">
              Intelligent thermal monitoring for neonatal care, saving lives through accessible technology.
            </p>
          </div>
          
          <div>
            <h3 className="font-semibold mb-4">Product</h3>
            <div className="space-y-2 text-sm">
              <Link to="/technology" className="block text-muted-foreground hover:text-foreground">Technology</Link>
              <Link to="/product" className="block text-muted-foreground hover:text-foreground">Features</Link>
              <Link to="/demo" className="block text-muted-foreground hover:text-foreground">Request Demo</Link>
            </div>
          </div>
          
          <div>
            <h3 className="font-semibold mb-4">Company</h3>
            <div className="space-y-2 text-sm">
              <Link to="/about" className="block text-muted-foreground hover:text-foreground">About Us</Link>
              <Link to="/contact" className="block text-muted-foreground hover:text-foreground">Contact</Link>
            </div>
          </div>
          
          <div>
            <h3 className="font-semibold mb-4">Contact</h3>
            <div className="space-y-2 text-sm text-muted-foreground">
              <p>info@thermovision-ai.com</p>
              <p>+1 (555) 123-4567</p>
            </div>
          </div>
        </div>
        
        <div className="border-t border-border mt-8 pt-8 text-center text-sm text-muted-foreground">
          <p>&copy; 2024 ThermoVision AI. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;