import pygame

class Visualization:
    def __init__(self):
        self.playing_animation = False
        self.current_node_index = 0
    
    def replay_animation(self):
        self.playing_animation = True
        self.current_node_index = 0
                        
    def visualize_graph(self, graph, all_paths):
        # Retrieve final path
        self.all_paths = all_paths
        self.path_list = all_paths.split(" -> ")
        self.path_list.insert(0, "1")  # Initialize start node
        
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()
    
        # Set up the window
        window_width = 800
        window_height = 800  # Increase the window height to add padding at the bottom
        margin = 100  # Set the desired margin size
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('Visualization of Maze')
        
        # Define colors
        color_mapping = {
            '10': (198, 115, 255),  # Purple
            '11': (255, 165, 0),    # Orange
            '13': (255, 165, 0),    # Orange
            '19': (50, 205, 50),    # Green
            '22': (50, 205, 50),    # Green
            '25': (255, 165, 0),    # Orange
            '33': (30, 144, 255),   # Blue
            '37': (50, 205, 50),    # Green
            '41': (255, 165, 0),    # Orange
            '43': (30, 144, 255),   # Blue
            '46': (198, 115, 255),  # Purple
            '52': (255, 165, 0),    # Orange
            '30': (255, 105, 180),  # Pink
            '31': (255, 105, 180),  # Pink
            '54': (255, 105, 180)   # Pink
        }
        default_color = (255, 192, 203)  # Pink
        node_radius = 20  # Set the desired radius for nodes
    
        # Find the minimum and maximum coordinates in the graph
        min_x = min(node.get_position()[0] for node in graph.nodes)
        max_x = max(node.get_position()[0] for node in graph.nodes)
        min_y = min(node.get_position()[1] for node in graph.nodes)
        max_y = max(node.get_position()[1] for node in graph.nodes)
    
        # Calculate the scaling factors
        scale_x = (window_width - 2 * margin - 2 * node_radius) / (max_x - min_x)
        scale_y = (window_height - 2 * margin - 2 * node_radius) / (max_y - min_y)
        
        # Animation settings
        delay = 500  # Delay between frames in milliseconds
        clock = pygame.time.Clock()
        
        # Clear the screen
        screen.fill((255, 255, 255))  # White background
        
        # Main game loop
        self.running = True
        
        while self.running:
            # Draw "Replay" button
            replay_button_width = 120
            replay_button_height = 30
            replay_button_margin = 40
            
            replay_button_rect = pygame.Rect((window_width - replay_button_width) // 2, 
                                             window_height - replay_button_height - replay_button_margin, 
                                             replay_button_width, replay_button_height)
            replay_button_color = (45, 44, 65)
            pygame.draw.rect(screen, replay_button_color, replay_button_rect)
            
            font = pygame.font.Font(None, 30)
            label = font.render('Replay', True, (255, 255, 255))
            button_label_x = replay_button_rect.centerx - label.get_width() // 2
            button_label_y = replay_button_rect.centery - label.get_height() // 2
            screen.blit(label, (button_label_x, button_label_y))
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if replay_button_rect.collidepoint(event.pos):
                        if not self.playing_animation:
                            self.replay_animation()
                            self.playing_animation = False
                
            # Draw nodes
            for i, node in enumerate(graph.nodes):
                # Check if node value exists in color_mapping, otherwise use default_color
                if node.get_value() in color_mapping:
                    node_color = color_mapping[node.get_value()]
                else:
                    node_color = default_color
                
                # Highlight the current node in the animation
                # if node.get_value() == self.path_list[self.current_node_index]:
                if self.current_node_index < len(self.path_list) and node.get_value() == self.path_list[self.current_node_index]:
                    node_color = (255, 0, 0)  # Red
                
                position = node.get_position()
                # Scale and translate the node coordinates
                scaled_x = int((position[0] - min_x) * scale_x + margin + node_radius)
                scaled_y = int((position[1] - min_y) * scale_y + margin + node_radius)
                pygame.draw.circle(screen, node_color, (scaled_x, scaled_y), node_radius)  # Draw a circle at scaled position
                
                # Draw node label
                font = pygame.font.Font(None, 30)
                label = font.render(f'{node.get_value()}', True, (0, 0, 0))
                screen.blit(label, (scaled_x - 10, scaled_y - 10))
    
                # Draw edges
                for neighbour in node.get_neighbours():
                    neighbour_position = neighbour.get_position()
                    # Scale and translate the neighbour coordinates
                    scaled_neighbour_x = int((neighbour_position[0] - min_x) * scale_x + margin + node_radius)
                    scaled_neighbour_y = int((neighbour_position[1] - min_y) * scale_y + margin + node_radius)
                    pygame.draw.line(screen, (0, 0, 0), (scaled_x, scaled_y), (scaled_neighbour_x, scaled_neighbour_y))
                    
            # Update the display
            pygame.display.flip()
            clock.tick(30)  # Limit the frame rate to 30 FPS
    
            # Delay between frames
            pygame.time.wait(delay)
            
            # Increment the current node index
            self.current_node_index += 1
            if self.current_node_index >= len(self.path_list):
                if self.playing_animation:
                    # Reset the current_node_index to replay from the beginning
                    self.replay_animation()
                    self.playing_animation = False
                else:
                    # Set current_node_index to the last node to stop at the end
                    self.current_node_index = len(self.path_list) - 1            
        
        pygame.quit()
